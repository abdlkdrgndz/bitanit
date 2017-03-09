# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0013_mekanlar_mekan_ekleyen'),
    ]

    operations = [
        migrations.AddField(
            model_name='mekanlar',
            name='mekan_onay',
            field=models.CharField(default='0', max_length=1, choices=[('0', '0'), ('1', '1')]),
        ),
    ]
