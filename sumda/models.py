from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    nickname = models.CharField(verbose_name='사용자 닉네임', max_length=50)


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    follower = models.ManyToManyField(
        User, related_name='follower', blank=True)
    following = models.ManyToManyField(
        User, related_name='following', blank=True)
    request = models.ManyToManyField(
        User, related_name='request', blank=True)

    def __str__(self):
        return self.user.nickname


class Diary(models.Model):
    objects = models.Manager()
    nickname = models.CharField(max_length=50)
    profile = models.ForeignKey(
        Profile, related_name='profile', on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(
        verbose_name='주소', max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    title = models.CharField(verbose_name='일기 제목',
                             max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    receiver = models.ManyToManyField(
        Profile, related_name='receiver', blank=True)
    block = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    objects = models.Manager()
    comment = models.TextField(blank=True, null=True)
    diary = models.ForeignKey(
        Diary, related_name='diary', on_delete=models.CASCADE, blank=True, null=True)
    nickname = models.CharField(max_length=50)
