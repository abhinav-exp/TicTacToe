from django.urls import path
from . import views

urlpatterns = [
	path('',views.bot,name ='bot'),
	path('channel',views.channel, name = 'channel'),
]
