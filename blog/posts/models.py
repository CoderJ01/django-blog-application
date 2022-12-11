from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100) # CharField is a String field
    body = models.CharField(max_length=1_000_000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)