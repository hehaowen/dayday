# coding=utf-8
from .models import *
from article import utils
from rest_framework import viewsets
from django.views.generic import ListView
from django.views.generic import TemplateView, DetailView
from .serializers import ArtSerializers, TitleSerializers


class IndexView(TemplateView):
    template_name = 'daydays/arite/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = TitleInfo.objects.all()
        context1 = {}
        for i in range(len(tags)):
            tag = TitleInfo.objects.filter(id=i)
            articsl = ArticlesInfo.objects.filter(sorts=i)[0:4]
            context1['tags%s' % i] = tag
            context1['artics%s' % i] = articsl
        context.update(context1)
        return context


class ArtDetailView(DetailView):
    model = ArticlesInfo
    template_name = 'daydays/arite/detail.html'
    context_object_name = 'artics'

    def get(self, request, *args, **kwargs):
        response = super(ArtDetailView, self).get(self, request, *args, **kwargs)
        self.object.clickup()
        aname_ids = request.session.get('aname_ids', '')
        aname_id = '%d' % self.object.id
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
        request.session['aname_ids'] = aname_ids
        return response

    def get_context_data(self, **kwargs):
        context = super(ArtDetailView, self).get_context_data(**kwargs)
        news = ArticlesInfo.objects.all()[0:4]
        context.update({
            'news': news
        })
        return context


class list(ListView):
    model = ArticlesInfo
    template_name = 'daydays/arite/list.html'
    context_object_name = 'artics'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(list, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        start, end = utils.custompaginator(paginator.num_pages, page.number, 4)
        context.update({
            'page_range': range(start, end + 1)
        })
        return context


class TitleSer(viewsets.ModelViewSet):
    queryset = TitleInfo.objects.all()
    serializer_class = TitleSerializers


class ArtSer(viewsets.ModelViewSet):
    queryset = ArticlesInfo.objects.all()
    serializer_class = ArtSerializers
