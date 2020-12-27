from django.urls import path
from . import views

urlpatterns = [
	path('room',views.room,name ='room'),
	path('roomchannel',views.roomchannel, name='roomchannel'),
	path('play',views.play,name='play'),
	path('playchannel',views.playchannel, name='playchannel'),
	path('rechannel',views.rechannel, name='rechannel')
]