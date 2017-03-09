# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0007_auto_20150913_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='mekanlar',
            name='mekan_adres',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mekanlar',
            name='mekan_telefon',
            field=models.PositiveIntegerField(default=12),
            preserve_default=False,
        ),
    ]
