from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Comment
#회원가입
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','nickname']

#댓글
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['nickname', 'comment']
