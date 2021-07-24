from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from .forms import SignupForm, CommentForm
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from urllib.parse import urlparse

from .models import *


def main(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
        posts = Diary.objects.filter(profile = profile)
        ctx = {
            'posts_list':posts
        }
    except:
        ctx = {

        }
    return render(request, 'main.html', ctx )

#상세보기 페이지 (댓글 폼)
def detail(request, pk):
    post = get_object_or_404(Diary, pk = pk)
    comment_list = Comment.objects.filter(diary=post)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.diary = post
            comment.save()
            return redirect('/detail/'+str(pk) )
    else :
        comment_form = CommentForm()
        
    return render(request, 'detail.html', {'post':post, 'comment_list':comment_list, 'comment_form':comment_form })
    

def send(request):
    recieved_diary = Diary.objects.filter(receiver=None)
    recieved_diary.receiver = request.user

# 로그인, 회원가입, 로그아웃 기능
def signup_view(request):
    if request.method=="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            new_profile = Profile()
            new_profile.user = user
            new_profile.save()
            return redirect('/')
    else:
        form=SignupForm()
    return render(request, 'signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password) 
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})
def logout_view(request):
	logout(request)
	return redirect('/')



def write(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if request.method == 'GET':

        return render(request, 'write.html')
    elif request.method == 'POST':

        new_diary = Diary()
        new_diary.nickname = request.POST['nickname']
        new_diary.profile = profile
        new_diary.content = request.POST['content']
        new_diary.title = request.POST['title']
        if request.POST['location']:
            new_diary.address = request.POST['location']
        else:
            pass
        new_diary.save()
        return redirect('/')


@csrf_exempt
def location(request):
    req = json.loads(request.body)
    latitude = req['latitude']
    longitude = req['longitude']
    address = req['address']
    user = request.user
    profile = Profile.objects.get(user=user)
    return JsonResponse({'latitude': latitude, 'longitude': longitude, 'address': address})

#others페이지 관리함수
def others(request):
    random_content = Diary.objects.order_by("?").first()
    user = request.user
    profile = Profile.objects.get(user=user)
    random_content.receiver.add(profile)
    contents = Diary.objects.filter(receiver=profile)
    return render(request, 'others.html', {'contents':contents })
