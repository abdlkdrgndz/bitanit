# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0009_mekanlar_mekan_yetkisili'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mekanlar',
            name='ip',
        ),
    ]
