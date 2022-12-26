from django.contrib import admin

# Register your models here.
from .models import Category, SubForum, Topic

admin.site.register(Category)
admin.site.register(SubForum)
admin.site.register(Topic)
