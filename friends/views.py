from django.shortcuts import render
from django.http import JsonResponse
import random, string

# Create your views here.
def room(request):
	print(request.POST)
	print(request.session.items())
	#cprint(request.session.set_expiry(0))
	return render(request,'room.html')

def roomchannel(request):
	if request.method == 'GET':
		room = "".join([random.choice(string.ascii_letters) for n in range(3)])
		
		return JsonResponse({"code":room})

def play(request,room_no):
	return render(request,'play.html',{'room_no':room_no})