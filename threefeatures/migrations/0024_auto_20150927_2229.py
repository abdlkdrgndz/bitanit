# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0023_auto_20150927_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofil',
            name='kullanici_id',
            field=models.CharField(max_length=20),
        ),
    ]
