from django.db import models
from django.contrib.auth.models import User

class GamingController(models.Model): ##Main model for the gaming controller
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    year = models.IntegerField(unique=False, blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/', blank=True)
    post_time = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.title}"
    
class Profile(models.Model):  ##Profile model for the user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"