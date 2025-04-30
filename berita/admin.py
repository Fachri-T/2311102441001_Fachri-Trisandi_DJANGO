from django.contrib import admin
from berita.models import Artikel, Kategori

# Register your models here.
admin.site.register(Kategori)

class ArtikelAdmin(admin.ModelAdmin):
    list_display = ['nama', 'speksifikasi']
    search_fields = ['nama']

admin.site.register(Artikel, ArtikelAdmin)