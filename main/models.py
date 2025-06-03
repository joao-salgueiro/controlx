from django.db import models
from django.contrib.auth.models import User

class GamingController(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    year = models.IntegerField(unique=False, blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/', blank=True)

    def __str__(self):
        return f"{self.title}"