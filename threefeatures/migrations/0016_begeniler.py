# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0015_auto_20150923_0127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Begeniler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('kullanici_id', models.PositiveIntegerField(verbose_name='Kullanıcı')),
                ('yildiz', models.PositiveIntegerField(verbose_name='Yıldız Sayısı')),
            ],
            options={
                'verbose_name_plural': 'Beğeniler',
                'verbose_name': 'Beğeni',
            },
        ),
    ]
