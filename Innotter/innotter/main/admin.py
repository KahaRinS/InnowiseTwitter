from django.contrib import admin
from main.models import Like, Page, Post, Tag

admin.site.register(Page)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Like)
