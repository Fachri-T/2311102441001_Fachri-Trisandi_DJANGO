from django.shortcuts import render
from django.http import HttpResponse
from berita.models import Artikel, Kategori


def home(request):
    template_name = 'halaman/index.html'
    data_artikel = Artikel.objects.all()
    data_kategori = Kategori.objects.all()
    context = {
        'title': 'Lost Vape',
        'data_artikel' : data_artikel,
        'data_kategori' : data_kategori
    }
    return render(request, template_name, context)


def about_us(request):
    template_name = 'halaman/about.html'
    context = {
        'title': 'About us',
        'welcome': 'ini page about',
    }
    return render(request, template_name, context)

def contact_us(request):
    template_name = 'halaman/contact.html'
    context = {
        'title': 'about me',
        'welcome': 'ini page about',
    }
    return render(request, template_name, context)

def detail_artikel(request, slug):
    template_name =  'halaman/detail_artikel.html'
    artikel = Artikel.objects.get(slug = slug)
    context = {
        'title' : artikel.nama,
        'artikel' : artikel
    }
    return render(request, template_name, context)
