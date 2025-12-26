from django.db import models
from django.contrib.auth.models import User

class Publication(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='publications/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publications')

    def __str__(self):
        return self.name
