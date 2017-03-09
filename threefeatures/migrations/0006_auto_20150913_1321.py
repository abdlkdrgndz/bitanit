# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0005_auto_20150913_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mekanlar',
            name='ip',
            field=models.GenericIPAddressField(),
        ),
    ]
