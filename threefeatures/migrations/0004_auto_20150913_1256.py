# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0003_auto_20150913_1254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sectiklerimiz',
            old_name='mekan_id',
            new_name='mekan_adi',
        ),
    ]
