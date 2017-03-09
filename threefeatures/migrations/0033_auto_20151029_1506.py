# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0032_ucretsiz_hizmetler_ilgili_hizmet_sure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ucretsiz_hizmetler',
            name='ilgili_hizmet_sure',
            field=models.DateField(auto_now=True, verbose_name='Fırsat Süresi', null=True),
        ),
    ]
