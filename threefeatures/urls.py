from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *
admin.autodiscover()

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="iskelet.html"),  name='anasayfa'),
    url(r'^mekanlar/$', MekanFiltrele, name='Mekan_Arama'),
    url(r'^mekan_listesi/$', Mekan_Listele.as_view(), name='Mekan_Listesi'),
    url(r'^mekan_sil/(?P<pk>[0-9]+)$', Mekan_Sil.as_view(), name='Mekan_Sil'),
    url(r'^mekan_duzenle/(?P<pk>[0-9]+)$', Mekan_Duzenle.as_view(), name='Mekan_Duzenle'),
    url(r'^detaylar/(?P<mekanad>.+)/(?P<gelen_id>[0-9]+)/$', MekanDetay, name='Mekan_Detaylar'),
    url(r'^login/$', Kullanici_Giris, name='Kullanici_Giris'),
    url(r'^logout/$', Cikis, name='Kullanici_Cikis'),
    url(r'^reg/$', TemplateView.as_view(template_name='registration/register.html'), name='Kullanici_Kayit'),
    url(r'^reg_control/$', Kullanici_Kayit, name='Kayit_Kontrol'),
    url(r'^kayit/$', Mekan_Kayit.as_view(template_name='kayit.html'), name='Mekan_Kayit_Sayfasi'),
    url(r'^kadi_sorgula/$', Kayitli_Kullanici_Sorgula, name='Kayitli_Kullanici_Sorgula'),
    url(r'^parola_kontrol/$', Eski_Parola_Kontrol, name='Eski_Parola_Kontrol'),
    url(r'^update_us/$', Kullanici_Bilgileri_Guncelle.as_view(), name='Kullanici_Bilgileri_Guncelle'),
    url(r'^change_pass/$', Parola_Degistir, name='Parola_Degistir'),
    url(r'^alan_sorgula/$', Hizmet_Tip_Sorgula, name='Hizmet_Tip_Sorgula'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^yildizla/', Begenilerim, name='yildizla'),
    url(r'^guvenlik_kodu/', Guvenlik_Kodu, name='gvk'),
    url(r'^abonelik/', Abone_Ol, name='abone'),
    url(r'^ucretsiz_talepler/', Ucretsiz_Hizmet_Talebi, name='ucretsiz_talepler'),

    url(r'^tara/(.+)$', Ad_Search, name='tara'),
    #url(r'^pub/$', MixWork, name='mix'),
    url(r'^trial/', MixWork, name='dene'),
    url(r'^adv/', Advenced_Work, name='adv'),
    url(r'^fora/', Listele.as_view(), name='obj'),
    url(r'^controls/', Calling, name='bibi'),
    url(r'^getting/', MyView.as_view(mesaj="oooooooo"), name='aag'),
    url(r'^yeniden/', Yeniden.as_view(), name='yeniden'),
    url(r'^yonlendir/', Yonlendirme.as_view(), name='yonlendir'),
    url(r'^sayfalama', sayfalama, name='sayfa'),
    url(r'^ekle', DbFunc, name='ekle'),
]

urlpatterns += staticfiles_urlpatterns()