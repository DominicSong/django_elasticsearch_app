from django.http import HttpResponse
from django.shortcuts import render
from .search import ElasticObj
from .data import SearchRes

def home(request):
    return HttpResponse('<p>Hello world!</p>')

def search_home(request):
    return render(request, 'search.html')

def search(request):
    request.encoding = 'utf-8'
    context = {}
    search_name = request.GET['q']
    if search_name == '':
        context['empty'] = 1
        return render(request, 'search.html', context)
    es = ElasticObj('test')
    search_res = es.search(search_name)
    obj_list = [SearchRes(item_dict['_source']) for item_dict in search_res]
    context['list'] = obj_list
    return render(request, 'search.html', context)
    