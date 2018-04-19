# coding=utf-8
from django.http import response
from django.shortcuts import render
from rest_framework import viewsets, filters
from .serializers import ArtSerializers, TitleSerializers
from .models import *


# Create your views here.
def index(request):
    tags1 = TitleInfo.objects.filter(id=1)
    tags2 = TitleInfo.objects.filter(id=2)
    tags3 = TitleInfo.objects.filter(id=3)
    tags4 = TitleInfo.objects.filter(id=4)
    tags5 = TitleInfo.objects.filter(id=5)
    artics1 = ArticlesInfo.objects.filter(sorts=1)[0:4]
    artics2 = ArticlesInfo.objects.filter(sorts=2)[0:4]
    artics3 = ArticlesInfo.objects.filter(sorts=3)[0:4]
    artics4 = ArticlesInfo.objects.filter(sorts=4)[0:4]
    artics5 = ArticlesInfo.objects.filter(sorts=5)[0:4]
    context = {'artics1': artics1,
               'artics2': artics2,
               'artics3': artics3,
               'artics4': artics4,
               'artics5': artics5,
               'tags1': tags1,
               'tags2': tags2,
               'tags3': tags3,
               'tags4': tags4,
               'tags5': tags5}
    print(context)
    return render(request, 'daydays/arite/index.html', context)


def detail(request, pk):
    artics = ArticlesInfo.objects.get(id=pk)
    news = ArticlesInfo.objects.all()
    aname_ids = request.session.get('aname_ids', '')
    aname_id = '%d' % artics.id
    if aname_ids != '':
        aname_ids1 = aname_ids.split(',')
        if aname_ids1.count(aname_id) >= 1:
            aname_ids1.remove(aname_id)
        aname_ids1.insert(0, aname_id)
        if len(aname_ids1) >= 6:
            del aname_ids1[5]
        aname_ids = ','.join(aname_ids1)
    else:
        aname_ids = aname_id
    context = {'artics': artics, 'news': news}
    request.session['aname_ids'] = aname_ids

    return render(request, 'daydays/arite/detail.html', context)


def list(request):
    artics = ArticlesInfo.objects.all()
    context = {'artics': artics}
    return render(request, 'daydays/arite/list.html', context)


class TitleSer(viewsets.ModelViewSet):
    queryset = TitleInfo.objects.all()
    serializer_class = TitleSerializers


class ArtSer(viewsets.ModelViewSet):
    queryset = ArticlesInfo.objects.all()
    serializer_class = ArtSerializers
