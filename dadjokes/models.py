from django.db import models

# Create your models here.


class Joke(models.Model):
    '''model for joke information'''
    text = models.TextField()
    name = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''return a string representation of the Joke'''
        return f'{self.name} : {self.text} '

class Picture(models.Model):
    '''model for pictures'''
    image_url = models.URLField(blank=True)
    name = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''return a string representation of the Picture'''
        return f'{self.name} : {self.image_url} '
