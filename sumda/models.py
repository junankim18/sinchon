from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    nickname = models.CharField(verbose_name='사용자 닉네임', max_length=50)


class Profile(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    follower = models.ManyToManyField(
        User, related_name='follower', blank=True)
    following = models.ManyToManyField(
        User, related_name='following', blank=True)
    request = models.ManyToManyField(
        User, related_name='request', blank=True)


class Diary(models.Model):
    objects = models.Manager()
    nickname = models.CharField(max_length=50)
    profile = models.ForeignKey(
        Profile, related_name='profile', on_delete=models.CASCADE)
    address = models.CharField(
        verbose_name='주소', max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    receiver = models.ForeignKey(
        Profile, related_name='receiver', on_delete=models.CASCADE, blank=True, null=True)


class Comment(models.Model):
    objects = models.Manager()
    comment = models.TextField(blank=True, null=True)
    diary = models.ForeignKey(
        Diary, related_name='diary', on_delete=models.CASCADE, blank=True, null=True)
    nickname = models.CharField(max_length=50)
