from django.urls import path
from .views import hello,health,DocumentListView,document_list_using_Serializer,DocumentCreateView


urlpatterns = [
    path('/', hello),
    path('health/',health),
    path('documents/',DocumentListView.as_view()),
    path('documents-serializer/<int:pk>/',document_list_using_Serializer),
    path('document/add/',DocumentCreateView.as_view()),
]