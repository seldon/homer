# Create your views here.

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import Http404
from news.models import News


def list(request):
    LIST_LIMIT = 8
    try:
        news_list = News.objects.all()[:LIST_LIMIT]
        context = { 'news_list' : news_list }
    except:
        raise Http404
    
    return render_to_response('news/news_list.html', context_instance=RequestContext(request, context))

    


def detail(request, slug):
    LIST_LIMIT = 12
    try:
        news_list = News.objects.all()[:LIST_LIMIT]
        new = News.objects.get(slug=slug)
    except:
        raise Http404
    
    context = { 'news_list' : news_list, 'new' : new }
    return render_to_response('news/news_detail.html', context_instance=RequestContext(request, context))
