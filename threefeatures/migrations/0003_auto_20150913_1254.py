# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0002_auto_20150912_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sectiklerimiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mekan_degerlendirme', models.CharField(max_length=120)),
                ('mekan_yildiz', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'Seçtiklerimiz',
            },
        ),
        migrations.AlterField(
            model_name='mekanlar',
            name='mekan_foto',
            field=models.ImageField(upload_to='assets/images/'),
        ),
        migrations.AddField(
            model_name='sectiklerimiz',
            name='mekan_id',
            field=models.ForeignKey(to='threefeatures.Mekanlar'),
        ),
    ]
