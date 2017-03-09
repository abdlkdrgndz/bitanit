from django.forms import ModelForm
from django import forms
from .models import Mekanlar, Hizmetler
from django import forms


class BegeniForm(forms.ModelForm):
    class Meta:
        model = Mekanlar
        fields = ['mekan_fiyat', 'mekan_adi', 'mekan_web_site']

class FormYeni(forms.ModelForm):
    class Meta:
        model  = Hizmetler
        fields = ['hizmet_adi']








