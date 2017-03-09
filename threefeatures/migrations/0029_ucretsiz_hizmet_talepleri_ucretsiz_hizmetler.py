# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0028_auto_20151010_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ucretsiz_Hizmet_Talepleri',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('uye_istek', models.CharField(max_length=50, verbose_name='Talep Eden Üye')),
                ('talep_edilen_hizmet', models.CharField(max_length=20, verbose_name='Talep Edilen Hizmet')),
                ('talep_tarih', models.DateTimeField(verbose_name='Talep Tarihi', auto_now=True)),
                ('talep_sonuc', models.CharField(max_length=25, verbose_name='Talep Durumu', choices=[('0', 'Onaylanmamış'), ('1', 'Talep kabul edildi.'), ('2', 'Talep reddedildi.')])),
            ],
            options={
                'verbose_name_plural': 'Ücretsiz Hizmet Talepleri',
                'verbose_name': 'Ücretsiz Hizmet Talebi',
            },
        ),
        migrations.CreateModel(
            name='Ucretsiz_Hizmetler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('tur', models.CharField(max_length=20, choices=[('0', 'Afiş'), ('1', 'Animasyon'), ('2', 'Intro')])),
                ('foto_video', models.FileField(upload_to='assets/images/ucretsizler/', verbose_name='Fotoğraf/Video')),
                ('aciklama', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Ücretsiz Hizmetler',
                'verbose_name': 'Ücretsiz Hizmet',
            },
        ),
    ]
