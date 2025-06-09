from django.db import models

class LocalTexts(models.Model): ## Model for storing local texts
    key = models.CharField(max_length=100, unique=True)  # Unique identifier for the text
    text = models.TextField()  # The actual text content

    def __str__(self):
        return f"{self.key}: {self.text[:50]}"  # Return a string representation of the model
