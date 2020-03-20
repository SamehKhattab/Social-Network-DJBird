# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetsapp', '0004_auto_20200318_1825'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='singletweet',
            options={'ordering': ['-timestamp']},
        ),
    ]
