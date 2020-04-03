# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userprofile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(default=b'profile_img/blueprofile2.png', null=True, upload_to=b'profile_img', blank=True),
        ),
    ]
