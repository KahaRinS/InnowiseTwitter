from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.name

class Page(models.Model):
    name = models.CharField(max_length=80,  unique=True)
    uuid = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    tags = models.ManyToManyField('main.Tag', related_name='pages', blank=True)
    owner = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='pages')
    followers = models.ManyToManyField('users.CustomUser', related_name='follows', blank=True)

    image = models.URLField(null=True, blank=True)

    is_private = models.BooleanField(default=False)
    follow_requests = models.ManyToManyField('users.CustomUser', related_name='requests', blank=True)
    unblock_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='posts')
    content = models.CharField(max_length=180)
    reply_to = models.ForeignKey('main.Post', on_delete=models.SET_NULL, null=True, blank=True, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.page}  {self.created_at}'