from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    '''data of a blog article'''

    title = models.TextField(blank=True)
    author = models.TextField(blank=True)
    text = models.TextField(blank=True)
    published = models.DateTimeField(auto_now=True)
    image_url = models.URLField(blank=True)
    
    def __str__(self):
        '''return a string representation of the article'''
        return f'{self.title} by {self.author} on {self.published}'
    
    def get_absolute_url(self):
        '''return the url to access a particular article instance'''
        return reverse('article', kwargs={'pk':self.pk})
    
    def get_all_comments(self):
        '''Return all of the comments about this article.'''
        comments = Comment.objects.filter(article=self)
        return comments
    
class Comment(models.Model):
    '''a comment on a blog article'''
    article = models.ForeignKey("Article", on_delete=models.CASCADE)
    author = models.TextField(blank=False)
    text = models.TextField(blank=False)
    published = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        '''Return a string representation of this Comment object.'''
        return f'{self.text}'