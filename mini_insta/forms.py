# file: mini_insta/forms.py
# Nicholas Zhang
# nzhan01@bu.edu
# created: 10/1/2025
# forms file containing all the forms for the mini_insta app


from django import forms
from .models import *


from django import forms
from .models import Profile, Post, Photo

class CreatePostForm(forms.ModelForm):
    '''a form for adding an post to the db'''
    #image_url = forms.URLField(required=False, label='Image URL')
    class Meta:
        '''associate the form with the Post model'''
        model = Post
        fields = [ 'caption'] 

class UpdateProfileForm(forms.ModelForm):
    ''' A form to update a profile in the database.'''

    class Meta:
        '''associate the form with the Profile model'''
        model = Profile
        fields = ['profile_image_url', 'display_name', 'bio_text']  #  fields from Profile model 