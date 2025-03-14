from django.contrib import admin
from user.models import Data

# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = ['user', 'alamat', 'telepon']
    search_fields = ['user__username']

admin.site.register(Data, DataAdmin)