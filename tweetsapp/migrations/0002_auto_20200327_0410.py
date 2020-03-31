# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweetsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='singletweet',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AddField(
            model_name='singletweet',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 27, 4, 10, 27, 480315, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='singletweet',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 27, 4, 10, 40, 413389, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='singletweet',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='singletweet',
            name='content',
            field=models.CharField(max_length=250),
        ),
    ]
