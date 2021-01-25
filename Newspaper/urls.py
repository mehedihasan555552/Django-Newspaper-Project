"""Newspaper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.sitemaps import GenericSitemap # new
from django.contrib.sitemaps.views import sitemap # new

from base.models import * # new

info_dict = {
    'queryset': LatestPost.objects.all(),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    # path('summernote/', include('django_summernote.urls')),
     path('sitemap.xml', sitemap, # new
        {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
        name='django.contrib.sitemaps.views.sitemap'),

    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
