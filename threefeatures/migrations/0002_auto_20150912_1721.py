# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hizmettipleri',
            old_name='hizmetler_id',
            new_name='hizmetler_adi',
        ),
    ]
