# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0024_auto_20150927_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mekanlar',
            name='mekan_fiyat',
            field=models.DecimalField(decimal_places=2, verbose_name='Mekan Minumum Hizmet Bedeli', max_digits=10, null=True),
        ),
    ]
