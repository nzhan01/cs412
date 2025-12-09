# project/app/adapters.py
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model
from .models import Professor

User = get_user_model()

class MySocialAccountAdapter(DefaultSocialAccountAdapter):

    def pre_social_login(self, request, sociallogin):
        """
        Called after Google authenticates but before the login is finalized.
        Use it to link Google account → existing Professor → existing User.
        """
        if sociallogin.is_existing:
            # Already linked — nothing to do
            return
        
        email = sociallogin.account.extra_data.get("email")
        if not email:
            return  # Should never happen with Google, but safe.

        # Try to find professor with matching email
        try:
            professor = Professor.objects.get(email__iexact=email)
        except Professor.DoesNotExist:
            return  # No professor → do not link automatically

        # Does professor already have a user?
        if professor.user:
            # Link Google login to existing user
            sociallogin.connect(request, professor.user)
            return

        # No user exists yet — create one and attach it
        user = sociallogin.user
        user.username = email.split("@")[0]
        user.email = email
        user.save()

        professor.user = user
        professor.save()
