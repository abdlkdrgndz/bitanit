# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0012_auto_20150918_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='mekanlar',
            name='mekan_ekleyen',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
