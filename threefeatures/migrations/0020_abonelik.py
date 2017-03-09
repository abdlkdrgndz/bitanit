# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0019_auto_20150926_0100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abonelik',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('eposta', models.EmailField(verbose_name='Abone E-Posta Adresi', max_length=254)),
            ],
            options={
                'verbose_name': 'E-Posta Adresi',
                'verbose_name_plural': 'E-Posta Adresleri',
            },
        ),
    ]
