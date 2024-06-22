from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import sync_to_async
from .models import MessagesUser
import time
import json
from .serializers import MessageSerializer
from rest_framework.response import Response


class GmailConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        # Получаем список сообщений из базы данных
        messages = await self.get_messages()
        progress = str(min(int(time.time() % 10 * 10), 100))+'%'
        # Отправляем список сообщений клиенту
        await self.send(text_data=json.dumps({
            'type': 'message_list',
            'messages': messages,
            'progress': progress
        }, default=str))

    @sync_to_async
    def get_messages(self):
        messages = list(MessagesUser.objects.values('id', 'description', 'user_id',
                                                    'attachments','sent_at',
                                                    'created_at','them_mail'))
        MessageSerializer(messages)
        return messages

