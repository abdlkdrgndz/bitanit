# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0017_begeniler_mekan_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mekanlar',
            name='mekan_adi',
            field=models.SlugField(verbose_name='Mekan Adı', max_length=120),
        ),
    ]
