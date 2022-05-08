# Generated by Django 4.0.1 on 2022-04-02 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0008_ip_newspost_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.RemoveField(
            model_name='like',
            name='reporter',
        ),
        migrations.RemoveField(
            model_name='newspost',
            name='likes',
        ),
        migrations.AddField(
            model_name='newspost',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='post_views', to='newsApp.Like', verbose_name='Вподобання'),
        ),
        migrations.AlterField(
            model_name='newspost',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='post_views', to='newsApp.Ip', verbose_name='Перегляди'),
        ),
    ]
