


from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Article
from .forms import CreateArticleForm
from .forms import CreateCommentForm
from django.urls import reverse

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
    

class CreateArticleView(CreateView):
    '''a view to create a new article'''
    #model = Article
    form_class = CreateArticleForm
    template_name = 'blog/create_article_form.html'
    #success_url = '/blog/'  # redirect to the list of articles after creation

class CreateCommentView(CreateView):
    '''A view to create a new comment and save it to the database.'''
 
 
    form_class = CreateCommentForm
    template_name = "blog/create_comment_form.html"

    ## show how the reverse function uses the urls.py to find the URL pattern
    def get_success_url(self) -> str:
        '''Return the URL to redirect to after successfully submitting form.'''
        #return reverse('show_all')
        ## note: this is not ideal, because we are redirected to the main page.

        # retrieve the PK from the URL pattern
        pk = self.kwargs['pk']
        # call reverse to generate the URL for this Article
        return reverse('article', kwargs={'pk':pk})
    
    def get_context_data(self):
        '''Return the dictionary of context variables for use in the template.'''
 
 
        # calling the superclass method
        context = super().get_context_data()
 
 
        # find/add the article to the context data
        # retrieve the PK from the URL pattern
        pk = self.kwargs['pk']
        article = Article.objects.get(pk=pk)
 
 
        # add this article into the context dictionary:
        context['article'] = article
        return context

    def form_valid(self, form):
        '''This method handles the form submission and saves the 
        new object to the Django database.
        We need to add the foreign key (of the Article) to the Comment
        object before saving it to the database.
        '''
        
		# instrument our code to display form fields: 
        #print(f"CreateCommentView.form_valid: form.cleaned_data={form.cleaned_data}")
        
        # retrieve the PK from the URL pattern
        pk = self.kwargs['pk']
        article = Article.objects.get(pk=pk)
        # attach this article to the comment
        form.instance.article = article # set the FK
 
 
        # delegate the work to the superclass method form_valid:
        return super().form_valid(form)