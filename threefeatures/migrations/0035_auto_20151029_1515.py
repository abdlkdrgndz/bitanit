# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0034_auto_20151029_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ucretsiz_hizmetler',
            name='ilgili_hizmet_sure',
            field=models.DateField(null=True, blank=True, verbose_name='Fırsat Süresi', auto_created=True),
        ),
    ]
