# Generated by Django 4.1.5 on 2023-01-31 13:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0004_alter_customuser_options_customuser_date_joined_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='title',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
