from django.conf.urls import url

from others import views

urlpatterns = [
    url(r'cart',views.cart,name='cart'),
    url(r'place_order',views.place_order,name='place_order'),
]