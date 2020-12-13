from django.urls import path
from . import views

urlpatterns = [
	path('room',views.room,name ='room'),
	path('roomchannel',views.roomchannel, name='roomchannel'),
	path('play<str:room_no>',views.play,name='play')
]