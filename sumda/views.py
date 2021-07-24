from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from .forms import SignupForm, CommentForm
from .models import *


def main(request):
    posts = Diary.objects.all()
    return render(request, 'main.html',  {'posts_list':posts})

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
            return redirect('detail', pk = pk)
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
            return redirect('main')
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
                return redirect('main')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})
def logout_view(request):
	logout(request)
	return redirect('main')


