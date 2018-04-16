from django.conf.urls import url
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'UserViewSet', views.UserViewSet, base_name="UserViewSet")

urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^register_handle/', views.register_handle, name='register_handle'),
    url(r'^login/', views.login, name='login'),
    url(r'^login_handle/', views.login_handle, name='login_handle'),
    url(r'^user_center_info/', views.user_center_info, name='user_center_info'),
    url(r'^user_center_order/', views.user_center_order, name='user_center_order'),
    url(r'^user_center_site/', views.user_center_site, name='user_center_site'),
    url(r'^user_center/', views.user_center, name='user_center'),
    url(r'^outlogin/', views.outlogin, name='outlogin'),
    url(r'^(?P<token>\w+.[-_\w]*\w+.[-_\w]*\w+)/$', views.active_user, name='active_user')
]
