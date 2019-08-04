from django.contrib import admin
from .models import *
# Register your models here.

class TweetOption(admin.ModelAdmin):
    list_display = ['id', 'author', 'created', 'updated']

admin.site.register(Tweet, TweetOption)