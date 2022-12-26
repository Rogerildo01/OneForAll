"""OneForAll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from apps.login.views import * 
from apps.cargo.views import *
from apps.cargo import views
from apps.home.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    #path('login/', loginIndex, name='loginIndex'),
    #path('cargo/', cargo , name = 'cargo'),
    path('cargo/cadastro/', cadastro , name = 'cadastro'),
    path('cargo/delete/<int:id_cargo>', deleteCargo, name = 'deleteCargo'),
    path('cargo/editar/<int:id_cargo>', editarCargo, name = 'editarCargo'),

    path('admin/', admin.site.urls),
    #path('home/', home , name = 'home'),
    path('', include('apps.login.urls')),
    path('', include('apps.home.urls')),
    path('', include('apps.cargo.urls')),

    #path('accounts/', include('django.contrib.auth.urls')),


] 

