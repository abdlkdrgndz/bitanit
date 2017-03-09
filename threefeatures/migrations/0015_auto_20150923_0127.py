# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threefeatures', '0014_mekanlar_mekan_onay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mekanlar',
            name='hizmet_id',
            field=models.ForeignKey(to='threefeatures.Hizmetler', verbose_name='Hizmet Alanı'),
        ),
        migrations.AlterField(
            model_name='mekanlar',
            name='hizmet_tip_id',
            field=models.ForeignKey(to='threefeatures.HizmetTipleri', verbose_name='Hizmet Tipi'),
        ),
        migrations.AlterField(
            model_name='mekanlar',
            name='il_id',
            field=models.ForeignKey(to='threefeatures.Iller', verbose_name='İl'),
        ),
        migrations.AlterField(
            model_name='mekanlar',
            name='mekan_adi',
            field=models.CharField(verbose_name='Mekan Adı', max_length=120),
        ),
        migrations.AlterField(
            model_name='mekanlar',
            name='mekan_adres',
            field=models.TextField(verbose_name='Mekan Adresi'),
        ),
        migrations.AlterField(
            model_name='mekanlar',
            name='mekan_eklenme_tarih',
            field=models.DateTimeField(auto_now=True, verbose_name='Mekan Eklenme/Guncellenme Tarihi'),
        ),
        migrations.AlterField(
            model_name='mekanlar',
            name='mekan_ekleyen',
            field=models.CharField(verbose_name='Mekan Ekleyen Kullanıcı', max_length=100),
        ),
        migrations.AlterField(
            model_name='mekanlar',
            name='mekan_fiyat',
            field=models.DecimalField(decimal_places=2, verbose_name='Mekan Minumum Hizmet Bedeli', max_digits=10),
        ),
        migrations.AlterField(
            model_name='mekanlar',
            name='mekan_foto',
            field=models.ImageField(upload_to='assets/images/mekanlar/', verbose_name='Mekan Fotoğrafı'),
        ),
        migrations.AlterField(
            model_name='mekanlar',
            name='mekan_onay',
            field=models.CharField(default='0', choices=[('0', '0'), ('1', '1')], verbose_name='Mekan Onay Durumu', max_length=1),
        ),
        migrations.AlterField(
            model_name='mekanlar',
            name='mekan_ozellik1',
            field=models.CharField(verbose_name='Mekan Özellik#1', max_length=20),
        ),
        migrations.AlterField(
            model_name='mekanlar',
            name='mekan_ozellik2',
            field=models.CharField(verbose_name='Mekan Özellik#2', max_length=20),
        ),
        migrations.AlterField(
            model_name='mekanlar',
            name='mekan_ozellik3',
            field=models.CharField(verbose_name='Mekan Özellik#3', max_length=20),
        ),
        migrations.AlterField(
            model_name='mekanlar',
            name='mekan_sahip_adi',
            field=models.CharField(verbose_name='Mekan Sahibi Adı', max_length=75),
        ),
        migrations.AlterField(
            model_name='mekanlar',
            name='mekan_sahip_eposta',
            field=models.EmailField(verbose_name='E-Posta Adresi', max_length=254),
        ),
        migrations.AlterField(
            model_name='mekanlar',
            name='mekan_tanitim',
            field=models.TextField(verbose_name='Mekan Tanıtım'),
        ),
        migrations.AlterField(
            model_name='mekanlar',
            name='mekan_telefon',
            field=models.PositiveIntegerField(verbose_name='Mekan Telefonu'),
        ),
        migrations.AlterField(
            model_name='mekanlar',
            name='mekan_web_site',
            field=models.URLField(verbose_name='Mekan Web Adresi'),
        ),
        migrations.AlterField(
            model_name='mekanlar',
            name='mekan_yetkisili',
            field=models.CharField(verbose_name='Mekan Yetkilisi', max_length=150),
        ),
    ]
