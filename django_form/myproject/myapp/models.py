from django.db import models

class UserEntry(models.Model):
    username = models.CharField(max_length=100)
    hobbies = models.TextField(blank=True)

    def __str__(self):
        return self.username
