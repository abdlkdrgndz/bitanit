# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0010_remove_mekanlar_ip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mekanlar',
            name='mekan_foto2',
        ),
        migrations.RemoveField(
            model_name='mekanlar',
            name='mekan_foto3',
        ),
        migrations.AlterField(
            model_name='sectiklerimiz',
            name='mekan_yildiz',
            field=models.PositiveIntegerField(choices=[('4', '4'), ('5', '5')]),
        ),
    ]
