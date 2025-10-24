# file: mini_insta/models.py
# Nicholas Zhang
# nzhan01@bu.edu
# created: 9/25/2025
# models file containing all the models for the mini_insta app


from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    '''data for a user profile'''
    username =models.TextField(blank=True)
    display_name = models.TextField(blank=True)
    profile_image_url =  models.URLField(blank=True)
    bio_text = models.TextField(blank=True)
    join_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 



    def __str__(self):
        '''return a string representation of the Profile'''
        return f'{self.display_name} : {self.bio_text} '
    
    def get_all_posts(self):
        '''Return all posts made by this profile.'''
        posts = Post.objects.filter(profile=self)
        posts = posts.order_by('timestamp')  
        return posts
    def get_absolute_url(self):
        # redirect to the Post detail page after creation
        return reverse("show_profile", kwargs={"pk": self.pk})
    
    def get_followers(self):
        '''Return all followers of this profile.'''
        followers = Follow.objects.filter(profile=self)

        follower_list = []
        for f in followers:
            follower_list.append(f.follower_profile)
        return follower_list
    
    def get_following(self):
        '''return all profiles this profile is following'''
        following = Follow.objects.filter (follower_profile=self)
        following_list = []
        for f in following:
            following_list.append(f.profile)
        return following_list
    
    def get_num_followers(self):
        '''return the number of followers this profile has'''
        return len(self.get_followers())
    
    def get_num_following(self):
        '''return the number of profiles this profile is following'''
        return len(self.get_following())
    
    def get_post_feed(self):
        '''return a feed of posts from profiles this profile follows'''
        following = self.get_following()
        feed_posts = Post.objects.filter(profile__in=following)
        feed_posts = feed_posts.order_by('-timestamp')
        return feed_posts


class Post(models.Model):
    '''data for a post'''
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    caption = models.TextField(blank=True)

    def __str__(self):
        '''return a string representation of the Post'''
        return f'{self.profile.username} @ {self.timestamp}: {self.caption} ' 
    

    def get_all_photos(self):
        '''Return all photos in this post.'''
        photos = Photo.objects.filter(post=self)
        photos = photos.order_by('timestamp')
        return photos
    
    def get_absolute_url(self):
        # redirect to the Post detail page after creation
        return reverse("show_post", kwargs={"pk": self.pk})
    
    def get_all_comments(self):
        '''return all comments for a post'''
        comments = Comment.objects.filter(post=self)
        return comments
    
    def get_likes(self):
        ''' get all likes for a post'''
        likes = Like.objects.filter(post=self)
        return likes


class Photo(models.Model):
    '''data for a photo'''
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    image_file = models.ImageField(blank=True) # an actual image

    
    def __str__(self):
        '''return a string representation of the Photo'''
        if self.image_file:
            return f'{self.post} @ {self.timestamp}: {self.image_file.url} '
        else:
            return f'{self.post} @ {self.timestamp}: {self.image_url} '
    
    def get_image_url(self):
        '''Return the image URL for this photo.'''
        if self.image_file:
            return self.image_file.url
        else:
            return self.image_url 
        
class Follow(models.Model):
    '''data for a follow relationship'''

    profile = models.ForeignKey("Profile" , related_name="profile", on_delete=models.CASCADE)
    follower_profile = models.ForeignKey("Profile", related_name="follower_profile", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''return a string representation of the Follow'''
        return f'{self.follower_profile.username} follows {self.profile.username} '
    

class Comment(models.Model):
    '''data for a comment on a post'''
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    text = models.TextField(blank=False)


    def __str__(self):
        '''return a string representation of the Comment'''
        return f'{self.profile} on {self.timestamp}: {self.text} '
    
class Like(models.Model):
    '''data for a like on a post'''
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''return a string representation of the Like'''
        return f'{self.profile} liked {self.post} on {self.timestamp} '