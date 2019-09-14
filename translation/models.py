from django.db import models

# Create your models here.

class Translation(models.Model):
    word = models.CharField(max_length=255, unique=True)
    meaning = models.TextField()
    example = models.TextField(null=True)

    def __str__(self):
        return f"{self.word} - {self.meaning}"