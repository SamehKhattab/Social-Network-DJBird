# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetsapp', '0004_singletweet_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='singletweet',
            name='reply',
            field=models.BooleanField(default=False, verbose_name=b'Is a reply?'),
        ),
    ]
