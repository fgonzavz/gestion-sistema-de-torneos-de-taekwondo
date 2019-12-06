"""gestion_sistema_torneos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from core import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_usuario, name='login'),
   path('login/autentificar/', views.autentificar, name='autentificar'),
    path('login/nuevo/', views.loginNuevo, name='loginNuevo'),
    path('home/', views.home, name='home'),
    path('equipos/', views.equipos, name='equipos'),
    path('calendario/', views.calendario, name='calendario'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('listado_equipos/', views.listadoEquipo, name='listado_equipos'),
    path('nuevoEquipo/', views.nuevoEquipo, name='nuevoEquipo'),
    path('modificar_equipo/<id>/', views.modificar_equipo, name='modificar_equipo'),
    path('eliminar_equipo/<id>/', views.eliminar_equipo, name='eliminar_equipo'),
    path('accounts/', include('django.contrib.auth.urls')),

    # path('base/', views.base, name='base'),
    # path('core/', ('django.views.static.serve',
    #    {'document_root': settings.MEDIA_ROOT}),name='core'),
    # (r'^core/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': settings.MEDIA_ROOT}),
]

admin.site.site_header = "Administración Sistema Gestion de Torneos"
admin.site.index_title = "Modulos de Administración"
admin.site.site_title = " Gestion de Torneos"


urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
