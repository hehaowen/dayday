"""dayday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
# from xadmin.plugins import xversion
# import xadmin

# version模块自动注册需要版本控制的 Model
# xversion.register_models()

# xadmin.autodiscover()
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
import xadmin
xadmin.autodiscover()
urlpatterns = [
                  # url(r'^admin/', include(admin.site.urls)),
                  url(r'^xadmin/', include(xadmin.site.urls)),
                  url(r'^user/', include('daydays.urls', namespace='daydays')),
                  url(r'', include('article.urls', namespace='article')),
                  url(r'^uploader', include('ckeditor_uploader.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
