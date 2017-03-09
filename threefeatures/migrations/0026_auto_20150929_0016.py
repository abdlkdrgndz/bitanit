# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0025_auto_20150929_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mekanlar',
            name='mekan_fiyat',
            field=models.DecimalField(max_digits=10, null=True, blank=True, verbose_name='Mekan Minumum Hizmet Bedeli', decimal_places=2),
        ),
    ]
