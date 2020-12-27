from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
import random, string
from .models import room_model
from datetime import datetime

#normal_time = 5*60
waiting_time = 10*60 
# Create your views here.
def room(request):
	return render(request,'room.html')

def makeroomready(room):
	room.last_t=datetime.now(tz=timezone.utc)
	room.no_people = 1
	room.state = "o"*9
	room.re = 0
	room.save()

def check_code(code):
	try :
		q = room_model.objects.get(name=code)
		model_time = int(q.last_t.strftime('%s'))
		print("model = "+str(model_time))
		now_time = int(datetime.now(tz=timezone.utc).strftime('%s'))
		print("now = "+str(now_time))
		if now_time - model_time > waiting_time:
			return True
		else:
			return False
	except :
		q = room_model.objects.create(name = code,last_t=datetime.now(tz=timezone.utc))
		q.save()
		return True

def check_code_post(code):
	try:
		q = room_model.objects.get(name=code)
		model_time = int(q.last_t.strftime('%s'))
		now_time = int(datetime.now(tz=timezone.utc).strftime('%s'))
		if now_time - model_time > waiting_time:
			#print(1)
			makeroomready(q)
			return 3
		elif q.no_people == 1:
			#print(3)
			q.last_t = datetime.now(tz=timezone.utc)
			q.no_people = 2
			q.save()
			return 2
		else:
			#print(4)
			return 1
	except:
		#print(5)
		q = room_model.objects.create(name = code, last_t=datetime.now(tz=timezone.utc))
		makeroomready(q)
		return 3


def roomchannel(request):
	if request.method == 'GET':
		code = "".join([random.choice(string.ascii_letters) for n in range(3)])
		while not check_code(code):
			code = "".join([random.choice(string.ascii_letters) for n in range(3)])
		makeroomready(room_model.objects.get(name=code))
		request.session['room_no']=code
		request.session['first']=True
		request.session.set_expiry(waiting_time)
		return JsonResponse({'code':code})
	else:
		code = request.POST.get('code')
		protocol = check_code_post(code)
		if protocol == 1:
			request.session.flush()
		elif protocol == 2:
			request.session['room_no']=code
			request.session['first']=False
			request.session.set_expiry(waiting_time)
		elif protocol == 3:
			request.session['room_no']=code
			request.session['first']=True
			request.session.set_expiry(waiting_time)
		return JsonResponse({'protocol':protocol})

def play(request):
	code = request.session.get('room_no','NONE')
	if code == 'NONE':
		return redirect('home')
	print(code)
	room = room_model.objects.get(name=code)
	room.last_t = datetime.now(tz=timezone.utc)
	room.save()
	def make_state_data1(ch):
		if ch=='o':
			return 0
		elif ch == 'f':
			return 1
		else:
			return 2
	def make_state_data2(ch):
		if ch=='o':
			return 0
		elif ch == 's':
			return 1
		else:
			return 2
	if request.session['first']:
		state_data = str(list(map(make_state_data1,room.state)))
	else:
		state_data = str(list(map(make_state_data2,room.state)))
	request.session.set_expiry(waiting_time)
	user_allow = False 
	sf = bool(room.state.count('s')-room.state.count('f'))
	if not (request.session['first'] ^ sf):
		user_allow = True
	return render(
		request,
		'play.html',
		{
			'room_no':room.name,
			'first':request.session['first'],
			'range3':[0, 1, 2],
			'state_data':state_data,
			'user_allow':user_allow
		})

def playchannel(request):
	#print('test0')
	code = request.session.get('room_no')
	room = room_model.objects.get(name=code)
	room.last_t = datetime.now(tz=timezone.utc)
	#room.save()
	request.session.set_expiry(waiting_time)
	#print('test')
	response_data = {}

	if request.method == 'POST':
		state_update = request.POST.get('state')
		print(state_update)

		def convert(a,b):
			s = []
			for u in state_update:
				if u == '1':
					s.append(a)
				elif u == '2':
					s.append(b)
				else:
					s.append('o')
			return "".join(s)
		print(request.session.items())
		print(room)
		if request.session['first'] :
			room.state = convert('f','s')
			#room.save()
		else :
			room.state = convert('s','f')
			#room.save()
		print(room)
	else:
		fc = room.state.count('f')
		sc = room.state.count('s')

		def convert(a,b,data):
			s = []
			for u in data:
				if u == 'f':
					s.append(a)
				elif u == 's':
					s.append(b)
				else:
					s.append('0')
			return "".join(s)

		if request.session['first']:
			if sc - fc == 1:
				response_data['update'] = True
				print(convert('1','2',room.state))
				response_data['state'] = convert('1','2',room.state)
			else :
				response_data['update'] = False
		else:
			if sc - fc == 0 and sc :
				response_data['update'] = True
				print(convert('2','1',room.state))
				response_data['state'] = convert('2','1',room.state)
			else :
				response_data['update'] = False
	room.save()
	return JsonResponse(response_data)

def rechannel(request):
	code = request.session['room_no']
	room = room_model.objects.get(name = code)
	room.last_t = datetime.now(tz=timezone.utc)
	response_data = {'re':False}
	if request.session['first']:
		if room.re == 3:
			print("first came re was 3 so made 0")
			room.re = 0
			response_data['re'] = True
			room.state = "o"*9
		elif room.re == 2:
			print("first came re was 2 so made 3")
			room.re = 3
			response_data['re'] = True
			room.state = "o"*9
		else:
			print("first came re was 0 so made 1")
			room.re = 1
	else:
		if room.re == 3:
			room.re = 0
			response_data['re'] = True
			room.state = "o"*9
			print("second came re was 3 so made 0")
		elif room.re == 1:
			room.re = 3
			response_data['re'] = True
			room.state = "o"*9
			print("second came re was 1 so made 3")
		else:
			room.re = 2
			print("second came re was 0 so made 2")
	print("room re "+str(room.re))
	room.save()
	request.session.set_expiry(waiting_time)
	return JsonResponse(response_data)







