from django.shortcuts import render
from .models import *


def main(request):
    return render(request, 'main.html')


def send(request):
    recieved_diary = Diary.objects.filter(receiver=None)
    recieved_diary.receiver = request.user
