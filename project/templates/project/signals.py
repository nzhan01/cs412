# signals.py
from django.dispatch import receiver
from allauth.socialaccount.signals import social_account_added
from django.contrib.auth.models import User
from models import Professor

@receiver(social_account_added)
def link_google_user(sender, request, sociallogin, **kwargs):
    user = sociallogin.user
    email = user.email

    try:
        professor = Professor.objects.get(email=email)
        professor.user = user
        professor.save()
        print("Linked Google account to Professor:", professor)
    except Professor.DoesNotExist:
        print("No professor with email", email)
