from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class MessagesUser(models.Model):
    them_mail = models.TextField()
    sent_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    attachments = models.TextField(blank=True, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
