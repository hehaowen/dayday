from django.conf.urls import url
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'art', views.ArtSer, base_name='art')
router.register(r'title', views.TitleSer, base_name='title')
app_name = 'comments'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^list', views.list.as_view(), name='list'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.ArtDetailView.as_view(), name='detail'),
]
