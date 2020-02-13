from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf
from .search import ElasticObj
from .data import SearchRes

def home(request):
    return HttpResponse('<p>Hello world!</p>')

def search_home(request):
    context = {}
    context.update(csrf(request))
    return render(request, 'search.html', context)

def search(request):
    request.encoding = 'utf-8'
    context = {}
    context.update(csrf(request))
    search_name = request.POST['q']
    search_fields = request.POST.getlist('field')
    if search_name == '':
        context['empty'] = 1
        return render(request, 'search.html', context)
    es = ElasticObj('test')
    search_res = es.search(search_name, search_fields)
    res_cnt = len(search_res)
    context['res_cnt'] = res_cnt
    obj_list = [SearchRes(item_dict['_source']) for item_dict in search_res]
    context['list'] = obj_list
    context['searched'] = 1
    return render(request, 'search.html', context)
    