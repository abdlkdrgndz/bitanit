# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0006_auto_20150913_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='mekanlar',
            name='mekan_foto2',
            field=models.ImageField(default='pic3.jpg', upload_to='assets/images/'),
        ),
        migrations.AddField(
            model_name='mekanlar',
            name='mekan_foto3',
            field=models.ImageField(default='pic3.jpg', upload_to='assets/images/'),
        ),
    ]
