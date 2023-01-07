from django.contrib import admin

# Register your models here.
from .models import Category, SubForum, Topic, TopicResponse


class SubForumAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'creator', 'created_at', 'is_active')

class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'subforum', 'creator', 'created_at', 'is_active')

class TopicResponseAdmin(admin.ModelAdmin):
    list_display = ('content_preview', 'topic', 'creator', 'created_at')

admin.site.register(Category)
admin.site.register(SubForum, SubForumAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(TopicResponse, TopicResponseAdmin)
