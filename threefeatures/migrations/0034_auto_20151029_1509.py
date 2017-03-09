# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0033_auto_20151029_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ucretsiz_hizmetler',
            name='ilgili_hizmet_sure',
            field=models.DateField(auto_created=True, null=True, verbose_name='Fırsat Süresi', auto_now=True),
        ),
    ]
