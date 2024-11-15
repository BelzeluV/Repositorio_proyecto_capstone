from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from Store.d_back import views as uservalidation




urlpatterns = [
#partes vitales del proyecto
    path('', include('Store.d_front.urls')),
    path('manager/', include('Store.d_back.urls')),
    path('MusicBook/', include('Library.urls')),
    path('MusicClass/', include('Classes.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

    path('registro/',                               uservalidation.registroUsuario,                           name = "registrarse"),
    path('validations/',                            uservalidation.ValidarUsuario,                            name = "validar"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




"""Z_Proyecto_Capstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
