from django.contrib import admin

from .models import Page, Post, Tag

admin.site.register(Page)
admin.site.register(Tag)
admin.site.register(Post)
