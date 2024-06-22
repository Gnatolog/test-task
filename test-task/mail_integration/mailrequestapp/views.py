from django.shortcuts import render
from django.views import (View)


# Create your views here.


class RequestMail(View):
    """
    Класс для загрузки писем с почты

    """

    def get(self, request):
        return render(request, 'mailrequestapp/mailrequest.html')





