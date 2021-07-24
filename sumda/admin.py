from django.contrib import admin
from .models import *


admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Diary)
admin.site.register(Comment)
