# Generated by Django 4.1.4 on 2022-12-28 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_post_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='main.page'),
        ),
    ]
