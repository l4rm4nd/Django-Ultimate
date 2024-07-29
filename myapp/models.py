from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid

'''
class Example(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name
'''