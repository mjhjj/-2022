# Generated by Django 4.0.1 on 2022-02-17 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0005_remove_newspost_likes_newspost_reporter_like_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='comment',
        ),
    ]
