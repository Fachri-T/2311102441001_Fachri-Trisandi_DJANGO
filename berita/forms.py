from django import forms
from berita.models import Artikel

class Katalogform(forms.ModelForm):

    class Meta:
        model = Artikel
        fields = ( 'nama', 'speksifikasi', 'kategori', 'thumbmail')
        widgets = {
            "nama" : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                }),
            "speksifikasi" : forms.Textarea(
                attrs = {
                    'class': 'form-control',
                }),
            "kategori" : forms.Select(
                attrs = {
                    'class': 'form-control',
                }),
        }