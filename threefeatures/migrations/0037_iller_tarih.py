# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0036_auto_20151029_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='iller',
            name='tarih',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
