# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0027_auto_20150929_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mekanlar',
            name='mekan_fiyat',
            field=models.CharField(blank=True, null=True, verbose_name='Mekan Minumum Hizmet Bedeli', max_length=12, default='Minumum Bedel Belirtilmemiştir.'),
        ),
        migrations.AlterField(
            model_name='mekanlar',
            name='mekan_telefon',
            field=models.CharField(max_length=14, verbose_name='Mekan Telefonu'),
        ),
        migrations.AlterField(
            model_name='mekanlar',
            name='mekan_web_site',
            field=models.URLField(blank=True, null=True, verbose_name='Mekan Web Adresi'),
        ),
    ]
