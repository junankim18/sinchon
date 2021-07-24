from django.contrib import admin
<<<<<<< HEAD
from .models import Diary, Comment
# Register your models here.

admin.site.register(Diary)
admin.site.register(Comment)
from .models import Diary, Comment
=======
from .models import *


admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Diary)
admin.site.register(Comment)
>>>>>>> b02a3b8fc3ad13c668a8908eafc352982257a22d
