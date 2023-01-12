from django.contrib import admin

from .models import Page,Tag,Post, Like

admin.site.register(Page)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Like)
