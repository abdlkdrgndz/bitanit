# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0030_auto_20151011_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='ucretsiz_hizmetler',
            name='ilgili_hizmet',
            field=models.ManyToManyField(to='threefeatures.HizmetTipleri'),
        ),
    ]
