from django.conf.urls import url
from rest_framework import routers
from others import views


router = routers.DefaultRouter()
router.register(r'otherViewset',views.otherViewset,base_name='otherViewset')


urlpatterns = [
    url(r'cart',views.cart,name='cart'),
    url(r'place_order',views.place_order,name='place_order'),
]