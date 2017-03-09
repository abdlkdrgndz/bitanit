# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0018_auto_20150926_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='mekanlar',
            name='slug',
            field=models.SlugField(default=1, max_length=290),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mekanlar',
            name='title',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mekanlar',
            name='mekan_adi',
            field=models.CharField(max_length=120, verbose_name='Mekan Adı'),
        ),
    ]
