# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0035_auto_20151029_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ucretsiz_hizmetler',
            name='ilgili_hizmet_sure',
            field=models.DateTimeField(null=True, auto_created=True, blank=True, verbose_name='Fırsat Süresi'),
        ),
    ]
