from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article
import random
# Create your views here.

class ShowAllView(ListView):
    '''define a view to show all articles'''

    model= Article
    template_name = 'blog/show_all.html'
    context_object_name = 'articles' # should be plural


class ArticleView(DetailView):
    '''display a single article'''
    model = Article
    template_name = 'blog/article.html'
    context_object_name = 'article' # should be singular


class RandomArticleView(DetailView):
    '''display a random article'''
    model = Article
    template_name = 'blog/article.html'
    context_object_name = 'article' # should be singular

    def get_object(self):
        '''return a random article'''
        all_articles = Article.objects.all()
        article = random.choice(all_articles)
        return article