# Generated by Django 4.0.1 on 2022-04-27 07:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0012_alter_newspost_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 27, 7, 58, 48, 107952, tzinfo=utc), verbose_name='Час'),
            preserve_default=False,
        ),
    ]