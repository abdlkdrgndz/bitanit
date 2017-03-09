# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0031_ucretsiz_hizmetler_ilgili_hizmet'),
    ]

    operations = [
        migrations.AddField(
            model_name='ucretsiz_hizmetler',
            name='ilgili_hizmet_sure',
            field=models.DateField(null=True, auto_now=True),
        ),
    ]
