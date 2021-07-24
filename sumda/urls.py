from django.urls import path, include
from .views import *


app_name = 'sumda'

urlpatterns = [
    path('', main, name='main'),
    path('write', write, name='write'),
    path('location/', location, name='location'),

]
