# Generated by Django 4.1.5 on 2023-01-31 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0016_remove_like_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='course',
        ),
        migrations.RemoveField(
            model_name='post',
            name='like',
        ),
        migrations.AddField(
            model_name='like',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='like', to='main.post'),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='posts', through='main.Like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
