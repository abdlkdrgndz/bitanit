# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0008_auto_20150916_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='mekanlar',
            name='mekan_yetkisili',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
