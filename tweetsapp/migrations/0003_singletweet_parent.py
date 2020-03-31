# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetsapp', '0002_auto_20200327_0410'),
    ]

    operations = [
        migrations.AddField(
            model_name='singletweet',
            name='parent',
            field=models.ForeignKey(blank=True, to='tweetsapp.SingleTweet', null=True),
        ),
    ]
