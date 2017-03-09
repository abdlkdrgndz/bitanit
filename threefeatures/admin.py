# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Hizmetler, HizmetTipleri,Iller, Mekanlar, Sectiklerimiz, Begeniler,Abonelik, UserProfil, Ucretsiz_Hizmetler, Ucretsiz_Hizmet_Talepleri

@admin.register(UserProfil)
class UserProfilAdmin(admin.ModelAdmin):
    list_display = ['kullanici_id', 'kullanici_ip']
    search_fields = ['kullanici_id']
    readonly_fields = ['kullanici_id','kullanici_ip']

@admin.register(Iller)
class IllerAdmin(admin.ModelAdmin):
    list_display = ['il_adi', 'tarih']
    search_fields = ['il_adi']


@admin.register(Hizmetler)
class HizmetlerAdmin(admin.ModelAdmin):
    list_display = ['id', 'hizmet_adi',]
    search_fields = ['hizmet_adi']


@admin.register(HizmetTipleri)
class HizmetTipleriAdmin(admin.ModelAdmin):
    list_display = ['id', 'hizmetler_adi', 'hizmet_tipi']
    search_fields = ['hizmet_tipi']


@admin.register(Mekanlar)
class MekanAdmin(admin.ModelAdmin):
    list_display = ['id', 'hizmet_id', 'hizmet_tip_id', 'il_id','mekan_sahip_adi',
                    'mekan_sahip_eposta','mekan_foto', 'mekan_adi','mekan_tanitim','mekan_web_site', 'mekan_telefon', 'mekan_fiyat', 'mekan_adres', 'mekan_yetkisili',
                    'mekan_ozellik1','mekan_ozellik2','mekan_ozellik3', 'mekan_ekleyen','mekan_onay']
    search_fields = ['mekan_adi']
    list_filter = ['mekan_onay']
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Sectiklerimiz)
class SectiklerimizAdmin(admin.ModelAdmin):
    list_display = ['mekan_adi', 'mekan_degerlendirme', 'mekan_yildiz', 'foto']
    search_fields = ['mekan_adi']

@admin.register(Begeniler)
class BegenilerAdmin(admin.ModelAdmin):
    list_display = ['kullanici_id', 'mekan_id', 'yildiz']
    search_fields = ['kullanici_id', 'yildiz']

@admin.register(Ucretsiz_Hizmetler)
class UcretsizHizmetlerAdmin(admin.ModelAdmin):
    list_display = ['id', 'tur', 'foto_video', 'aciklama', 'coklu_gosterim', 'ilgili_hizmet_sure']
    search_fields = ['tur', 'aciklama']


@admin.register(Ucretsiz_Hizmet_Talepleri)
class UcretsizTaleplerAdmin(admin.ModelAdmin):
    list_display = ['id', 'uye_istek', 'talep_edilen_hizmet' ,'talep_tarih', 'talep_sonuc']
    search_fields = ['uye_istek', 'talep_edilen_hizmet' ,'talep_tarih', 'talep_sonuc']
    list_filter = ['talep_sonuc']






