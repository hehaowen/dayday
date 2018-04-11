from django.conf.urls import url
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'art', views.ArtSer, base_name='art')
router.register(r'title', views.TitleSer, base_name='title')

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list', views.list, name='list'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]
