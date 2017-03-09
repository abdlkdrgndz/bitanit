# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hizmetler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hizmet_adi', models.CharField(help_text='Hizmet Adını Girin. Ör: Eğitim', max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Hizmetler',
                'verbose_name': 'Hizmet',
            },
        ),
        migrations.CreateModel(
            name='HizmetTipleri',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hizmet_tipi', models.CharField(max_length=60)),
                ('hizmetler_id', models.ForeignKey(to='threefeatures.Hizmetler')),
            ],
            options={
                'verbose_name_plural': 'Hizmet Tipleri',
                'verbose_name': 'Hizmet Tipi',
            },
        ),
        migrations.CreateModel(
            name='Iller',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('il_adi', models.CharField(help_text='İl Adını Girin', max_length=40)),
            ],
            options={
                'verbose_name_plural': 'İller',
                'verbose_name': 'İl',
            },
        ),
        migrations.CreateModel(
            name='Mekanlar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mekan_sahip_adi', models.CharField(max_length=75)),
                ('mekan_sahip_eposta', models.EmailField(max_length=254)),
                ('mekan_foto', models.ImageField(upload_to='images/')),
                ('mekan_adi', models.CharField(max_length=120)),
                ('mekan_tanitim', models.TextField()),
                ('mekan_web_site', models.URLField()),
                ('mekan_fiyat', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mekan_ozellik1', models.CharField(max_length=20)),
                ('mekan_ozellik2', models.CharField(max_length=20)),
                ('mekan_ozellik3', models.CharField(max_length=20)),
                ('mekan_eklenme_tarih', models.DateTimeField(auto_now=True)),
                ('ip', models.IPAddressField()),
                ('hizmet_id', models.ForeignKey(to='threefeatures.Hizmetler')),
                ('hizmet_tip_id', models.ForeignKey(to='threefeatures.HizmetTipleri')),
                ('il_id', models.ForeignKey(to='threefeatures.Iller')),
            ],
            options={
                'verbose_name_plural': 'Mekanlar',
                'verbose_name': 'Mekan',
            },
        ),
    ]
