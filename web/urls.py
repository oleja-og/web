"""web URL Configuration

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
from django.contrib import admin
from django.urls import path, re_path
from firstapp import views
from django.views.generic import TemplateView

urlpatterns = [
    path('home/',views.home),
    re_path(r'^products/$', views.products),
    re_path(r'^products/(?P<productid>\d+)/', views.products),
    path('users/', views.users),
    path('users/<int:id>/<str:name>/', views.users),
    re_path(r'^details', views.details),
    path('about', TemplateView.as_view(template_name='firstapp/about.html')),
    path('contact', views.contact),
    path('', views.index),
    path('index_app1', views.index_app1),
    path('admin/', admin.site.urls),
]
