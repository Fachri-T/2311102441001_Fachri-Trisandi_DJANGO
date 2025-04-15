from django.contrib import admin
from django.urls import path, include

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import  settings

from main.views import home, about

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('dashboard/', include("berita.urls")),
]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)