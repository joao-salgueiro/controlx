from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from allauth.socialaccount.signals import social_account_added



from main.models import Profile



@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(social_account_added)
def populate_profile_picture(request, sociallogin, **kwargs):
    user = sociallogin.user
    picture_url = sociallogin.account.extra_data.get('picture')

    if picture_url:
        profile, _ = Profile.objects.get_or_create(user=user)
        profile.profile_picture = picture_url
        profile.save()
