# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweetsapp', '0005_singletweet_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='singletweet',
            name='unliked',
            field=models.ManyToManyField(related_name='unliked', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
