from django.urls import path,include
from .views import StartPageView
from .import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', StartPageView.as_view(), name='start_page'),
    path('register/', views.register, name='register'),

]
