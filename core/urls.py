from django.urls import path
from .views import hello,health,index


urlpatterns = [
    path('/', hello),
    path('health/',health),
    path('index/', index)
]