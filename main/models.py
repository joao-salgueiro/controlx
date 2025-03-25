from django.db import models

class GamingController(models.Model):
    year = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/', blank=True)

    def __str__(self):
        return f"{self.year} - {self.title}"
