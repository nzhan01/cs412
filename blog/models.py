from django.db import models

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