from django.shortcuts import render

# Create your views here.

from .models import * 
from django.utils.http import urlunquote


class Arttype(object):
    def __init__(self,name,num):
        self.name = name
        self.num = num

def home(request):
    latest_art = Article.objects.order_by('-art_pub_date')[0]
    context = {'latest_art':latest_art}
    return render(request,'home/home.html',context)

def index(request):
    latest_art_list = Article.objects.order_by('-art_pub_date')[:3]
    art_type_list = findtype()
    context = {'latest_art_list' : latest_art_list, 'art_type_list':art_type_list}
    return render(request, 'index/index.html', context)

def article_id(request, article_id):
    article = Article.objects.get(pk=article_id)
    context = {'article':article}
    return render(request,'article/article_id.html', context)

def article_type(request,article_type):
    cur_art_type = urlunquote(article_type)
    article_list = Article.objects.filter(art_type=cur_art_type)
    art_type_list = findtype()
    context = {'latest_art_list':article_list, 'art_type_list':art_type_list,'art_type':cur_art_type}
    return render(request, 'article/article_type.html', context)

def findtype():
    art_list = Article.objects.all()
    art_type_name_list = []
    art_type_list = []

    for art in art_list:
        if not art.art_type in art_type_name_list:
            art_type_name_list.append(art.art_type)

    for art_type_name in art_type_name_list:
        art_type_list.append(Arttype(art_type_name, len(list(Article.objects.filter(art_type=art_type_name)))))

    return art_type_list