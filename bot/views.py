from django.shortcuts import render
from django.http import JsonResponse
from .bot_logic import main

# Create your views here.
def bot(request):
	return render(request,'bot.html',{
	'range3':[0,1,2]
	})

def channel(request):
	#print(request.POST)
	#help(request.POST)
	v = request.POST.get('data')
	print(v)
	#print(v.split(""))
	T = [[int(u) for u in v[3*i:3*i+3]] for i in range(3)]
	print(T)
	res = main(T)
	print(res)
	return JsonResponse({'ok':res})
