"""TNA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'twitterBootStrapExample', views.twitterBootStrapExample, name='twitterBootStrapExample'),
    url(r'verticalCollapse', views.verticalCollapse, name='verticalCollapse'),
    url(r'sideBar', views.sideBar, name='sideBar'),
    url(r'carrousel1', views.carrousel1, name='carrousel1'),
    url(r'grayscale', views.grayscale, name='grayscale'),
    url(r'landing', views.landing, name='landing'),
    url(r'carrousel', views.carrousel, name='carrousel'),
    url(r'tna', views.tna, name='tna'),

]
