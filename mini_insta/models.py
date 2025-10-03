# file: mini_insta/models.py
# Nicholas Zhang
# nzhan01@bu.edu
# created: 9/25/2025
# models file containing all the models for the mini_insta app


from django.db import models
from django.urls import reverse

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
    
    def get_all_posts(self):
        '''Return all posts made by this profile.'''
        posts = Post.objects.filter(profile=self)
        posts = posts.order_by('timestamp')  
        return posts
    

class Post(models.Model):
    '''data for a post'''
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    caption = models.TextField(blank=True)

    def __str__(self):
        '''return a string representation of the Post'''
        return f'{self.profile} @ {self.timestamp}: {self.caption} ' 
    

    def get_all_photos(self):
        '''Return all photos in this post.'''
        photos = Photo.objects.filter(post=self)
        photos = photos.order_by('timestamp')
        return photos
    
    def get_absolute_url(self):
        # redirect to the Post detail page after creation
        return reverse("show_post", kwargs={"pk": self.pk})


class Photo(models.Model):
    '''data for a photo'''
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''return a string representation of the Photo'''
        return f'{self.post} @ {self.timestamp}: {self.image_url} '