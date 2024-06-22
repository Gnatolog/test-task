from rest_framework import serializers
from .models import MessagesUser


class MessageSerializer(serializers.ModelSerializer):



    class Meta:
        model = MessagesUser
        fields = ('id', 'them_mail',
                  'sent_at', 'created_at',
                  'description', 'attachments')
