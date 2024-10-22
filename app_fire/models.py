from django.db import models

class Question(models.Model):
    text = models.TextField()
    answer = models.TextField(blank=True)

    def __str__(self):
        return self.text