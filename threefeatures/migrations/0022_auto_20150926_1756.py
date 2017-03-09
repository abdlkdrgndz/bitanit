# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0021_auto_20150926_1755'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abonelik',
            options={'verbose_name_plural': 'Abonelikler', 'verbose_name': 'Abonelik'},
        ),
        migrations.AlterModelOptions(
            name='begeniler',
            options={'verbose_name_plural': 'Beğeniler', 'verbose_name': 'Beğeni'},
        ),
    ]
