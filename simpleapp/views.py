from django.views.generic import ListView
from .models import Product
from django.shortcuts import render
from .models import Post
from .models import News


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'default.html'
    context_object_name = 'products'


class NewsListView(ListView):
    model = News
    ordering = '-pub_date'
    template_name = 'news_list.html'
    context_object_name = 'news_list'


def news_list(request):
    news = Post.objects.filter(is_news=True).order_by('-published_date')
    return render(request, 'news_list.html', {'news': news})


def news_detail(request, news_id):
    news = Post.objects.get(pk=news_id)
    return render(request, 'news_detail.html', {'news': news})