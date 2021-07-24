from django.urls import path, include
from .views import *
from . import views


app_name = 'sumda'

urlpatterns = [
    path('', main, name='main'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('detail/<int:pk>', views.detail, name="detail"),
    path('write', write, name='write'),
    path('mypage', mypage, name='mypage'),
    path('follow/<int:user_pk>/<int:diary_pk>', follow, name='follow'),
    path('accept/<int:pk>', accept, name='accept'),
    path('reject/<int:pk>', reject, name='reject'),


]
