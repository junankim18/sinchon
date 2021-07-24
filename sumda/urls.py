from django.urls import path, include
from .views import *
from . import views


app_name = 'sumda'

urlpatterns = [
    path('', main, name='main'),
<<<<<<< HEAD
    path('signup/',views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('detail/<int:pk>', views.detail, name="detail"),
=======
    path('write', write, name='write'),
    path('location/', location, name='location'),

>>>>>>> b02a3b8fc3ad13c668a8908eafc352982257a22d
]
