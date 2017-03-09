# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import *
from django.contrib.sessions.models import Session
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse, reverse_lazy, resolve
from django.db.models import Count, Q, Avg, Max, Empty
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, Http404, HttpResponsePermanentRedirect
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.template.defaultfilters import register,formats
from django.views.decorators.csrf import csrf_protect, csrf_exempt, requires_csrf_token
from django.views.decorators.http import require_http_methods
from django.views.generic import DetailView, CreateView, ListView, DeleteView, UpdateView, View, TemplateView, \
    RedirectView
import json
from .models import *
from braces.views import LoginRequiredMixin
# from django.contrib.auth.hashers import PBKDF2PasswordHasher
# from django.contrib.auth.forms import PasswordChangeForm
from .forms import *



# Bu tanımlama ile tüm sayfalara bunu gönderiyoruz. Context_Procerors ayarına ekleyelim. { 'threefeatures.views.serve_all' }
def serve_all(request):
    il_sorgula = Iller.objects.all().order_by('il_adi')
    hizmet_sorgula = Hizmetler.objects.all().order_by('hizmet_adi')
    sectiklerimiz_sorgula =  Sectiklerimiz.objects.all().order_by('?')[:4]
    yeni_katilanlar = Mekanlar.objects.raw('select avg(threefeatures_begeniler.yildiz) as yildizim, threefeatures_mekanlar.* from threefeatures_begeniler inner join threefeatures_mekanlar on threefeatures_begeniler.mekan_id=threefeatures_mekanlar.id WHERE mekan_onay="1" GROUP BY threefeatures_begeniler.mekan_id ORDER BY threefeatures_mekanlar.id DESC')[:20]
    mekanlar = Mekanlar.objects.raw('select avg(threefeatures_begeniler.yildiz) as yildizim, threefeatures_mekanlar.* from threefeatures_begeniler inner join threefeatures_mekanlar on threefeatures_begeniler.mekan_id=threefeatures_mekanlar.id WHERE mekan_onay="1" GROUP BY threefeatures_mekanlar.mekan_adi ORDER BY threefeatures_mekanlar.hizmet_tip_id_id')[:4]

    ucretsiz_hizmetler = Ucretsiz_Hizmetler.objects.all().order_by('-id')


    # KAYITLARI SAYMA
    hizmetleri_say = Hizmetler.objects.all().count()
    hizmet_turleri = HizmetTipleri.objects.all().count()
    mekan_say = Mekanlar.objects.all().count()

    ## FIRSAT EKLE ALANI
    if request.user.is_authenticated():
        kadi = request.user.id
        sorgula = Mekanlar.objects.filter(mekan_ekleyen=kadi).count()
        if sorgula > 0:
            sonuc_durum = 'basarili'
        else:
            sonuc_durum = 'basarisiz'
    else:
        sonuc_durum = 'üye girişi yapılmamış'

    return {'il_listesi' : il_sorgula , 'hizmet_listesi' : hizmet_sorgula, 'secilenler_listesi' : sectiklerimiz_sorgula, 'mekanlar' : mekanlar, 'yeni_katilanlar' : yeni_katilanlar, 'hizmet_say' : hizmetleri_say, 'hizmet_turleri' : hizmet_turleri, 'mekan_say' : mekan_say, 'ucretsiz_hizmetler' : ucretsiz_hizmetler, 'sonuc_durum' : sonuc_durum}

def MekanFiltrele(request):
    if request.method != 'POST':
        return redirect(reverse('Sorgular'))
    Mekan_Filtrele_Sonuc = Mekanlar.objects.filter(il_id__il_adi = request.POST.get('iller'), hizmet_id__hizmet_adi = request.POST.get('hizmetler'), mekan_adi__contains=request.POST.get('aramalar'), mekan_onay="1")
    if Mekan_Filtrele_Sonuc is not None:
        return render_to_response('mekan_sorgula.html', {'mekan_sonuclari' : Mekan_Filtrele_Sonuc},
                              context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect(reverse('anasayfa'))

def MekanDetay(request, mekanad, gelen_id):
    mekan_detay = Mekanlar.objects.raw('select avg(threefeatures_begeniler.yildiz) as yildizim, threefeatures_mekanlar.* from threefeatures_begeniler inner join threefeatures_mekanlar on threefeatures_begeniler.mekan_id=threefeatures_mekanlar.id WHERE threefeatures_mekanlar.id='+ gelen_id)
    return render_to_response("mekan_detaylar.html", {'mekan_detay' : mekan_detay}, context_instance=RequestContext(request) )

def Kullanici_Giris(request):
    kullanici_adi= request.POST['giris_eposta']
    parola = request.POST['giris_sifre']
    mekanlar = Mekanlar.objects.all().order_by('?')[:4]

    if '@' in kullanici_adi:
        if User.objects.filter(email=kullanici_adi).count() > 0:
            kontrol = User.objects.get(email=request.POST['giris_eposta'])
            kullanici = auth.authenticate(username=kontrol, password=parola)
            if kullanici is not None and kullanici.is_active:
                auth.login(request, kullanici)
                request.session['kadi_id'] = kullanici.id
                return render_to_response("iskelet.html", {'kullanici' : kullanici, 'mekanlar' : mekanlar}, context_instance=RequestContext(request))
            else:
                return render_to_response("iskelet.html", {'kullanici_yok' : 'Kullanıcı Kaydı Bulunamadı', 'mekanlar' : mekanlar }, context_instance=RequestContext(request))
        else:
            return render_to_response("iskelet.html", {'kullanici_yok' : 'Kullanıcı Kaydı Bulunamadı', 'mekanlar' : mekanlar }, context_instance=RequestContext(request))
    else:
        kullanici = auth.authenticate(username=kullanici_adi, password=parola)
        if kullanici is not None and kullanici.is_active:
            auth.login(request, kullanici)
            request.session['kadi_id'] = kullanici.id
            return HttpResponseRedirect(reverse('anasayfa'))
        else:
            return render_to_response("iskelet.html", {'kullanici_yok' : 'Kullanıcı Kaydı Bulunamadı', 'mekanlar' : mekanlar }, context_instance=RequestContext(request))

def Cikis(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('anasayfa'))

def Kullanici_Kayit(request):
    kadi = request.POST.get('kadi').strip()
    eposta = request.POST.get('eposta').strip()
    sifre = request.POST.get('sifre').strip()

    if kadi and eposta and sifre:
        if len(sifre) < 6:
            return render_to_response("registration/register.html", {'hata' : 'Lütfen şifrenizi doğru giriniz.'}, context_instance=RequestContext(request))
        else:
            kontrol = User.objects.filter(Q(username=kadi) | Q(email=eposta)).count()
            if kontrol > 0 :
                return render_to_response("registration/register.html", {'hata2' : 'Kayıtlı bir e-posta adresi yada kullanıcı adı girdiniz.'}, context_instance=RequestContext(request))
            else:
                kayit = User.objects.create_user(kadi, eposta, sifre)
                kullanici = auth.authenticate(username=kadi, password=sifre)
                auth.login(request, kullanici)
                request.session['kadi_id'] = kullanici.id
                kadi_ip = request.META['REMOTE_ADDR']
                kullanici_profil_kayit = UserProfil(kullanici_id= request.session['kadi_id'], kullanici_ip=kadi_ip).save()
                return render_to_response("registration/register.html", {'kullanici' : kullanici , 'basarili' : 'Kayıt İşleminiz Gerçekleşti.'}, context_instance=RequestContext(request))

@csrf_exempt
def Hizmet_Tip_Sorgula(request):
    if request.is_ajax():
        sorgu = HizmetTipleri.objects.filter(hizmetler_adi__id = request.POST['veri'])
        liste = list(sorgu.values_list('id', 'hizmet_tipi', flat=False))
        json_as = json.dumps(liste)
        return HttpResponse(json_as, content_type="application/json")

class Mekan_Kayit(CreateView, LoginRequiredMixin):
    model = Mekanlar
    fields = ['title', 'hizmet_id', 'hizmet_tip_id', 'il_id', 'mekan_sahip_adi', 'mekan_sahip_eposta', 'mekan_foto', 'mekan_adi','mekan_tanitim','mekan_web_site', 'mekan_telefon', 'mekan_fiyat', 'mekan_adres',
              'mekan_ozellik1', 'mekan_yetkisili', 'mekan_ozellik2', 'mekan_ozellik3', 'mekan_ekleyen']
    template_name = 'kayit.html'
    success_url = '/mekan_listesi'

    def get_queryset(self):
        s = Mekanlar.objects.filter(mekan_ekleyen=self.request.session['kadi_id'])
        return s

    def get_initial(self):
        if self.request.POST:
            mekan_max = Mekanlar.objects.latest('id').id
            _son_id = int(mekan_max) + 1
            k = Begeniler(kullanici_id=self.request.user.id, mekan_id=_son_id, yildiz="1").save()
            return k

class Mekan_Listele(ListView, LoginRequiredMixin):
    model = Mekanlar
    context_object_name = 'mekan_listesi'
    template_name = 'mekan_listesi.html'


    def get_queryset(self):
        s = Mekanlar.objects.filter(mekan_ekleyen=self.request.session['kadi_id'])
        return s



class Mekan_Sil(DeleteView, LoginRequiredMixin):
    model = Mekanlar
    success_url = reverse_lazy('Mekan_Listesi')
    context_object_name = 'sil'
    template_name = 'mekan_listesi.html'

    def get_queryset(self):
        s = Mekanlar.objects.filter(mekan_ekleyen=self.request.session['kadi_id'])
        return s

class Mekan_Duzenle(UpdateView, LoginRequiredMixin):
    model = Mekanlar
    success_url = reverse_lazy('Mekan_Listesi')
    context_object_name = 'guncelle'
    fields = ['hizmet_id', 'hizmet_tip_id', 'il_id','mekan_sahip_adi',
                    'mekan_sahip_eposta', 'mekan_foto', 'mekan_adi', 'mekan_tanitim','mekan_web_site', 'mekan_telefon', 'mekan_fiyat', 'mekan_adres', 'mekan_yetkisili',
                    'mekan_ozellik1','mekan_ozellik2','mekan_ozellik3']
    template_name = 'mekan_listesi.html'

    def get_queryset(self):
        s = Mekanlar.objects.filter(mekan_ekleyen=self.request.session['kadi_id'])
        return s

class Kullanici_Bilgileri_Guncelle(UpdateView, LoginRequiredMixin):
    model = User
    fields = ['username', 'email']
    success_url = reverse_lazy('anasayfa')

    def get_object(self, queryset=None):
        u = User.objects.get(id=self.request.session['kadi_id'])
        return u

def Parola_Degistir(request):
    kadi = request.user
    u = User.objects.get(username__exact=kadi)
    u.set_password(request.POST.get('password1'))
    u.save()
    return render_to_response("iskelet.html", {"parola_degisti" : "Parolanız değiştirildi."}, context_instance=RequestContext(request))

@csrf_exempt
def Kayitli_Kullanici_Sorgula(request):
    if request.is_ajax():
        sorgu = User.objects.filter(username = request.POST['veri']).count()
        json_as = json.dumps(sorgu)
        return HttpResponse(json_as, content_type="application/json")

@csrf_exempt
def Eski_Parola_Kontrol(request):
    if request.is_ajax():
        u = User.objects.get(id = request.POST.get('veri'))
        gonderilen=request.POST.get('eski_parola')
        if u.check_password(gonderilen) == True:
            deger = "Eski parola doğru girildi."
            json_as = json.dumps(deger)
            return HttpResponse(json_as, content_type="application/json")
        else:
            json_as = json.dumps("Eski parolanızı hatalı girdiniz.")
            return HttpResponse(json_as, content_type="application/json")


@csrf_exempt
def Begenilerim(request):
    if request.is_ajax():
        if request.user.is_authenticated():
            kadim = User.objects.get(id = request.user.id)
            yildizim=request.POST['yildiz']
            mekanim = request.POST['mekan']
            sorgula  = Begeniler.objects.filter(Q(kullanici_id = kadim.id), Q(mekan_id=mekanim)).count()
            if sorgula > 0 :
                Begeniler.objects.filter(Q(kullanici_id = kadim.id), Q(mekan_id=mekanim)).update(yildiz=yildizim)
            else:
                be = Begeniler(kullanici_id=kadim.id, mekan_id=mekanim, yildiz = yildizim).save()
                if be:
                    json_as = json.dumps('Oy verme işlemi gerçekleşti')
                    return HttpResponse(json_as, content_type="application/json")
                else:
                    json_as = json.dumps('Beklenmeyen bir hata oluştu.')
                    return HttpResponse(json_as, content_type="application/json")
        else:
            json_as = json.dumps("Oy vermek için lütfen üye olunuz.")
            return HttpResponse(json_as, content_type="application/json")


@csrf_exempt
def Guvenlik_Kodu(request):
    if request.is_ajax():
        import random
        sifre_harf = ['w', 'W', 'Q', 'q', 'X', 'x', 'T', 't', 'Z','z', 'M','m', 'Y', 'y']
        sayi1 = random.randint(1,12)
        sayi2 = random.randint(2,10)
        sayi3 = random.randint(4,9)
        sayi4 = random.randint(5,11)
        uretilen_sifre = str(sifre_harf[sayi1]) + str(sifre_harf[sayi4]) + str(sayi3) + str(sifre_harf[sayi3]) + str(sifre_harf[sayi2])
        json_as = json.dumps(uretilen_sifre)
        return HttpResponse(json_as, content_type="application/json")

@csrf_exempt
def Abone_Ol(request):
    if request.is_ajax():
        kontrol =Abonelik.objects.filter(eposta=request.POST['abone_eposta']).count()
        if kontrol > 0:
            json_as = json.dumps('Daha önce abone oldunuz.')
            return HttpResponse(json_as, content_type="application/json")
        else:
            kaydet = Abonelik(eposta=request.POST.get('abone_eposta')).save()
            json_as = json.dumps('Abonelik işleminiz tamamlandı.')
            return HttpResponse(json_as, content_type="application/json")


@csrf_exempt
def Ucretsiz_Hizmet_Talebi(request):
    if request.is_ajax():
        kontrol = Ucretsiz_Hizmet_Talepleri.objects.filter(uye_istek=request.POST['aktif_kadi']).count()
        if kontrol > 1:
            json_as = json.dumps('Talebiniz daha önce iletildi.')
            return HttpResponse(json_as, content_type="application/json")
        else:
            kaydet = Ucretsiz_Hizmet_Talepleri(uye_istek=request.POST['aktif_kadi'], talep_edilen_hizmet=request.POST['ucretsiz_hizmet']).save()
            json_as = json.dumps('Talebiniz gönderildi.')
            return HttpResponse(json_as, content_type="application/json")

class Ad_Search:
    def __init__(self):
        self.sites = []
        self.elements = ('span', 'div', 'a', 'h1', 'p')
        self.classes = ((''), (''), (''), (''), (''))

    def Scan(self, query):
        import requests
        for i in self.sites:
            site = requests.get(i.format(query))
            site_icerik = site.text
            soup = BeautifulSoup(site_icerik, "html.parser")
            soup.find_all(self.elements, )
            sonuclar = {'kitap_adi' : self.elements0, 'yazar': self.elements1, 'universite' : self.elements2, 'aciklama': self.elements4}
            return HttpResponse(sonuclar)


def MixWork(request):
    out = BegeniForm()
    return render_to_response("deneme.html", locals())


from django.db import transaction

@transaction.non_atomic_requests(using='other')
def Advenced_Work(request):
    from django.db.models import Avg, Min
    sorgula = Mekanlar.objects.aggregate(Max('mekan_fiyat'), Avg('mekan_fiyat'),  Min('mekan_fiyat') )
    aciklama  = Mekanlar.objects.annotate(num_authors=Count('mekan_fiyat'))
    ilk = Mekanlar.objects.annotate(Count('mekan_fiyat'))
    val = Mekanlar.objects.values('mekan_fiyat')
    farkli = Mekanlar.objects.get(mekan_adi__contains="patika")
    return render_to_response("deneme.html",
                              {'max': sorgula['mekan_fiyat__max'],
                               'min' : sorgula.get('mekan_fiyat__min'),
                               'avg' : sorgula.get('mekan_fiyat__avg'),
                               'cont' : aciklama,
                               'ilk' : ilk[0].mekan_fiyat__count,
                               'degerler' :  val,
                               'pat': farkli.mekan_sahip_eposta}

                              ) ## burada istersek bir dictionary i sorgula['mekan_fiyat__avg'] şeklinde de çıktısını gösterebiliriz.



class Listele(ListView):
    model = Mekanlar
    template_name = "listele.html"
    context_object_name = "veriler"



class Oyuncu():
    def __init__(self, isim, rütbe):
        self.rütbe = rütbe
        self.isim = isim
        self.pow =  74

    def puan_kazan(self):
        return HttpResponse('puan kazandın')

oyuncu = Oyuncu('Cemil', '3')

class Asker(Oyuncu):
    def __init__(self, *args): # *args yukarıda isim ve rütbeyi tek tek yazmaktansa bu şekilde de yazabiliriz.
        super().__init__(*args) # değiştirmek istemediğimiz değerleri aynı şekilde muhafaza etmek için kullandık.
        self.pow = 90

    def hareket_et(self):
        return HttpResponse(super().puan_kazan())  # yine burada super ile üst sınıftaki fonksiyona eriştik. istersek yeni özellikler de ekleyebiliriz.


nesne = Asker('Ahmet', '5')


def Calling(request):
    return  HttpResponse(nesne.hareket_et())


class MyView(View):
    mesaj = "Helloooo {}".format("ali dayiii")
    # url yapısında url(r'^getting/', MyView.as_view(mesaj="oooooooo"), name='aag') mesajı istediğimiz şekilde belirleyebiliriz.
    def get(self, request):
        return HttpResponse(self.mesaj)



class Yeniden(TemplateView):
    template_name = "404.html"


    def get_context_data(self, **kwargs):
        context = super(Yeniden, self).get_context_data(**kwargs)
        context['last'] = Hizmetler.objects.all()[:5]
        return context


class Yonlendirme(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        sorgula = get_object_or_404(Hizmetler, hizmet_adi= "Bebek")
        return HttpResponse('Var')


def sayfalama(request):
    sorgu = Mekanlar.objects.all()
    sayfa = Paginator(sorgu, 2)

    sayfa_sayisi = sayfa.num_pages  ## 2li bölmeye göre toplam sayfa sayısı
    toplam_veri = sayfa.count  ## mekanların toplam sayısı
    aralik = sayfa.page_range
    veriler = sayfa.page(1)

    gelen =  request.GET.get('s')
    if gelen:
        try:
            if int(gelen) > sayfa_sayisi:
                veriler = sayfa.page(1)
            else:
                veriler = sayfa.page(gelen)
        except EmptyPage:
            veriler = sayfa.gelen(1)

    return render_to_response("sayfalama.html" , locals(), context_instance=RequestContext(request))

def DbFunc(request):
    mekan =  Mekanlar.objects.get(hizmet_id__hizmet_adi="Tatil")
    mekan.mekan_tanitim = "Daha nice günlere"
    mekan.save()
    return render_to_response("sayfalama.html", {'formlar' : FormYeni(), 'hizmet' : mekan}, context_instance=RequestContext(request))






