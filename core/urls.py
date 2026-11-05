from django.urls import path
from .views import hello,health,DocumentListView,DocumentListUsingSerializer,DocumentCreateView


urlpatterns = [
    path('/', hello),
    path('health/',health),
    path('documents/',DocumentListView.as_view()),
    path('documents-serializer/<int:pk>/',DocumentListUsingSerializer.as_view()),
    path('document/add/',DocumentCreateView.as_view()),
]