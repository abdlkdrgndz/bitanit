# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0020_abonelik'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='begeniler',
            options={'verbose_name_plural': 'Abonelikler', 'verbose_name': 'Abonelik'},
        ),
    ]
