import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from urllib.parse import urlparse
from django.shortcuts import render, redirect
from .models import *


def main(request):
    return render(request, 'main.html')


def send(request):
    recieved_diary = Diary.objects.filter(receiver=None)
    recieved_diary.receiver = request.user


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
