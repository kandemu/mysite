from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SMS(models.Model):
    from_number = models.CharField(max_length = 20)
    to_number = models.CharField(max_length = 20)
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.body

