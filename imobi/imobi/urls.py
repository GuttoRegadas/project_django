from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

#import plataforma

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('autenticacao.urls')),
    path('', include('plataforma.urls')),
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    #path('admin/', admin.site.urls), # admin site
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)