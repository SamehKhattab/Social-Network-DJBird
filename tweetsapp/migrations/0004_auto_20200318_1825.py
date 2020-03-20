# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetsapp', '0003_auto_20200311_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singletweet',
            name='content',
            field=models.CharField(max_length=250),
        ),
    ]
