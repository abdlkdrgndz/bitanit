# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.utils import timezone
from django.db import models, IntegrityError
from django.contrib.auth.models import User


class UserProfil(models.Model):
    kullanici_id = models.CharField(max_length=20)
    kullanici_ip = models.GenericIPAddressField()

    def __str__(self):
        return self.kullanici_id + self.kullanici_ip

    class Meta:
        verbose_name = "Kullanıcı Profili"
        verbose_name_plural = "Kullanıcı Profilleri"

class Iller(models.Model):
    il_adi = models.CharField(max_length=40, help_text='İl Adını Girin')
    tarih = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return  self.il_adi



    class Meta:
        verbose_name = 'İl'
        verbose_name_plural = 'İller'

class Hizmetler(models.Model):
    hizmet_adi = models.CharField(max_length=80, help_text='Hizmet Adını Girin. Ör: Eğitim')

    def __str__(self):
        return  str(self.hizmet_adi)

    class Meta:
        verbose_name = 'Hizmet'
        verbose_name_plural = 'Hizmetler'

class HizmetTipleri(models.Model):
    hizmetler_adi = models.ForeignKey(Hizmetler)
    hizmet_tipi = models.CharField(max_length=60)

    def __str__(self):
        return  self.hizmet_tipi

    class Meta:
        verbose_name = 'Hizmet Tipi'
        verbose_name_plural = 'Hizmet Tipleri'

class Mekanlar(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=290, unique=False)
    hizmet_id = models.ForeignKey(Hizmetler, verbose_name='Hizmet Alanı')
    hizmet_tip_id = models.ForeignKey(HizmetTipleri, verbose_name='Hizmet Tipi')
    il_id = models.ForeignKey(Iller, verbose_name='İl')
    mekan_sahip_adi = models.CharField(max_length=75, verbose_name='Mekan Sahibi Adı')
    mekan_sahip_eposta = models.EmailField(verbose_name='E-Posta Adresi')
    mekan_foto =  models.ImageField(upload_to='assets/images/mekanlar/', verbose_name='Mekan Fotoğrafı')
    mekan_adi = models.CharField(max_length=120, verbose_name='Mekan Adı')
    mekan_tanitim = models.TextField(verbose_name='Mekan Tanıtım')
    mekan_web_site = models.URLField(verbose_name='Mekan Web Adresi', null=True, blank=True)
    mekan_telefon = models.CharField(max_length=14, verbose_name='Mekan Telefonu')
    mekan_fiyat = models.CharField(max_length=12, verbose_name='Mekan Minumum Hizmet Bedeli', null=True, blank=True, default='Minumum Bedel Belirtilmemiştir.')
    mekan_yetkisili = models.CharField(max_length=150, verbose_name='Mekan Yetkilisi')
    mekan_adres = models.TextField(verbose_name='Mekan Adresi')
    mekan_ozellik1 = models.CharField(max_length=20, verbose_name='Mekan Özellik#1')
    mekan_ozellik2 = models.CharField(max_length=20, verbose_name='Mekan Özellik#2')
    mekan_ozellik3 = models.CharField(max_length=20, verbose_name='Mekan Özellik#3')
    mekan_eklenme_tarih = models.DateTimeField(auto_now=True, verbose_name='Mekan Eklenme/Guncellenme Tarihi')
    mekan_ekleyen = models.CharField(max_length=100, verbose_name='Mekan Ekleyen Kullanıcı')
    mekan_onay = models.CharField(choices=(('0', '0'), ('1', '1')), max_length=1, default='0', verbose_name='Mekan Onay Durumu')

    def __str__(self):
        return self.mekan_adi

    def clean(self):
        if not self.mekan_sahip_eposta.endswith(end="@mynet.com"):
            raise ValidationError('Bu e-posta adresi geçersiz.')
        super(Mekanlar,self).clean()

    def save(self):
            """Auto-populate an empty slug field from the MyModel name and
            if it conflicts with an existing slug then append a number and try
            saving again.
            """
            import re
            from django.template.defaultfilters import slugify

            if not self.slug:
                self.slug = slugify(self.title)

            while True:
                try:
                    super(Mekanlar, self).save()
                # Assuming the IntegrityError is due to a slug fight
                except IntegrityError:
                    match_obj = re.match(r'^(.*)-(\d+)$', self.slug)
                    if match_obj:
                        next_int = int(match_obj.group(2)) + 1
                        self.slug = match_obj.group(1) + '-' + str(next_int)
                    else:
                        self.slug += '-2'
                else:
                    break



    class Meta:
        verbose_name = 'Mekan'
        verbose_name_plural = 'Mekanlar'


class Sectiklerimiz(models.Model):
    secim = (('4', '4'), ('5','5'))
    mekan_adi  = models.ForeignKey(Mekanlar)
    mekan_degerlendirme = models.TextField(max_length=120)
    mekan_yildiz = models.CharField(max_length=2, choices=secim)

    def __str__(self):
        return str(self.mekan_adi)

    def foto(self):
        return str(self.mekan_adi.mekan_foto)

    class Meta:
        verbose_name = 'Seçtiklerimiz'
        verbose_name_plural = 'Seçtiklerimiz'
        ordering = ['-mekan_adi']


class Begeniler(models.Model):
    kullanici_id = models.PositiveIntegerField(verbose_name='Kullanıcı')
    mekan_id = models.PositiveIntegerField(verbose_name='Mekan')
    yildiz = models.PositiveIntegerField(verbose_name='Yıldız Sayısı')

    def __str__(self):
        return str(self.kullanici_id)

    class Meta:
        verbose_name = 'Beğeni'
        verbose_name_plural = 'Beğeniler'


class Abonelik(models.Model):
    eposta = models.EmailField(verbose_name='Abone E-Posta Adresi')

    def __str__(self):
        return self.eposta

    class Meta:
        verbose_name="E-Posta Adresi"
        verbose_name_plural="E-Posta Adres"


class Ucretsiz_Hizmetler(models.Model):
    turler = (('0', 'Afiş'), ('1', 'Animasyon'), ('2', 'Intro'))
    tur  = models.CharField(choices=turler, max_length=20)
    foto_video = models.FileField(upload_to="ucretsizler/", verbose_name="Fotoğraf/Video")
    aciklama = models.CharField(max_length=150)
    ilgili_hizmet = models.ManyToManyField(HizmetTipleri)
    ilgili_hizmet_sure = models.DateTimeField(auto_now=False, auto_created=True, null=True, blank=True, verbose_name='Fırsat Süresi')


    def __str__(self):
        return self.tur

    def coklu_gosterim(self):
        return ', '.join([ other.hizmet_tipi for other in self.ilgili_hizmet.all() ])
    coklu_gosterim.short_description = 'Tavsiye Edilen Hizmet'
    coklu_gosterim.allow_tags = True

    class Meta:
        verbose_name="Ücretsiz Hizmet"
        verbose_name_plural="Ücretsiz Hizmetler"


class Ucretsiz_Hizmet_Talepleri(models.Model):
    sonuc= (
        ('0', ('Onaylanmamış')),
        ('1', ('Talep kabul edildi.')),
        ('2', ('Talep reddedildi.'))
    )
    uye_istek = models.CharField(max_length=50, verbose_name="Talep Eden Üye")
    talep_edilen_hizmet = models.CharField(max_length=20, verbose_name="Talep Edilen Hizmet")
    talep_tarih = models.DateTimeField(auto_now=True, verbose_name="Talep Tarihi")
    talep_sonuc= models.CharField(max_length=25, choices=sonuc, verbose_name="Talep Durumu")

    def __str__(self):
        return str(self.talep_tarih) + str(self.talep_tarih)

    class Meta:
        verbose_name="Ücretsiz Hizmet Talebi"
        verbose_name_plural="Ücretsiz Hizmet Talepleri"










