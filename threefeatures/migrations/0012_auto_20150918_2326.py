# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0011_auto_20150918_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mekanlar',
            name='mekan_foto',
            field=models.ImageField(upload_to='assets/images/mekanlar/'),
        ),
        migrations.AlterField(
            model_name='sectiklerimiz',
            name='mekan_yildiz',
            field=models.CharField(max_length=2, choices=[('4', '4'), ('5', '5')]),
        ),
    ]
