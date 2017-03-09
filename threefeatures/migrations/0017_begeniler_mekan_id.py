# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0016_begeniler'),
    ]

    operations = [
        migrations.AddField(
            model_name='begeniler',
            name='mekan_id',
            field=models.PositiveIntegerField(default=1, verbose_name='Mekan'),
            preserve_default=False,
        ),
    ]
