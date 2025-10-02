from django import forms
from .models import Article, Comment

class CreateArticleForm(forms.ModelForm):
    '''a form for adding an article to the db'''
    class Meta:
        '''associate the form with the Article model'''
        model = Article
        fields = ['author', 'title', 'text', 'image_url'] 

class CreateCommentForm(forms.ModelForm):
    '''A form to add a Comment to the database.'''
 
 
    class Meta:
        '''associate this form with the Comment model; select fields.'''
        model = Comment
        #fields = ['article', 'author', 'text', ]  # which fields from model should we use
        fields = ['author', 'text', ]  # which fields from model should we use