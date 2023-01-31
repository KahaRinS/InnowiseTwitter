from django.contrib import admin

from main.models import Page, Post, Tag, Like

admin.site.register(Page)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Like)
