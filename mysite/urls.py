"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from .views import home_view, SongsListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home_view),
    url(r'^allsongs/$', SongsListView.as_view()),
    url(r'^albumHindi/', include('GrabHindiSongs.urls')),
    url(r'^albumPanjabi/', include('GrabPanjabiSongs.urls')),
    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots_file"),
    url(r'^sitemap.xml$', TemplateView.as_view(template_name="sitemap.xml", content_type="xml"), name="siteMap_file"),
    url(r'^allsongs/sitemap.xml$', TemplateView.as_view(template_name="sitemap.xml", content_type="xml"), name="siteMap_file"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)