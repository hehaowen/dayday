from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from daydays.models import UserInfo
from .models import OthersInfo
from .serializers import OtherSerializer


def cart(request):
    return render(request,'daydays/others/cart.html')

def place_order(request):
    cname = request.session.get('username')
    name = UserInfo.objects.filter(username=cname)
    context = {'user':name}
    return render(request,'daydays/others/place_order.html',context)

class otherViewset(viewsets.ModelViewSet):
    queryset = OthersInfo.objects.all()
    serializer_class = OtherSerializer