from django.urls import path
from .views import RequestMail

urlpatterns = [
    path('requestmail/',RequestMail.as_view(), name='request_mail'),

]
