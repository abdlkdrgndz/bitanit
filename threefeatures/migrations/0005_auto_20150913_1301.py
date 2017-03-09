# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0004_auto_20150913_1256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sectiklerimiz',
            options={'ordering': ['-mekan_adi'], 'verbose_name_plural': 'Seçtiklerimiz', 'verbose_name': 'Seçtiklerimiz'},
        ),
        migrations.AlterField(
            model_name='sectiklerimiz',
            name='mekan_degerlendirme',
            field=models.TextField(max_length=120),
        ),
    ]
