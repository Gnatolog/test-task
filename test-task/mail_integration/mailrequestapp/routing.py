from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from .consumers import GmailConsumer

websocket_urlpatterns =[
        path('ws/gmail/', GmailConsumer.as_asgi()),
]