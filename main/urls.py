from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('room/<str:lobby>/', lobby, name='lobby'),
    path('sing_up/', sing_up, name='sing_up'),
	path('sing_in/', sing_in, name='sing_in'),
]