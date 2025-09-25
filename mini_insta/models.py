# file: mini_insta/models.py
# Nicholas Zhang
# nzhan01@bu.edu
# created: 9/25/2025
# models file containing all the models for the mini_insta app


from django.db import models

# Create your models here.

class Profile(models.Model):
    '''data for a user profile'''
    username =models.TextField(blank=True)
    display_name = models.TextField(blank=True)
    profile_image_url =  models.URLField(blank=True)
    bio_text = models.TextField(blank=True)
    join_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        '''return a string representation of the Profile'''
        return f'{self.display_name} : {self.bio_text} '