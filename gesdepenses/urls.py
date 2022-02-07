from django.urls import path

from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('init/', views.seed, name='seed'),
	path('minus/', views.minus, name= 'minus'),
	path('plus/', views.plus, name= 'plus'),
	path('dele/', views.dele, name= 'dele'),
	path('login/', views.entrer, name = 'login'),
	path('connect/', views.connect, name = 'connect'),
	path('disconnect/', views.disconnect, name = 'disconnect'),
]