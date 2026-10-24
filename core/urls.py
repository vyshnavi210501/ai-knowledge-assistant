from django.urls import path
from .views import hello,health,document_list,document_list_using_Serializer,add_document


urlpatterns = [
    path('/', hello),
    path('health/',health),
    path('documents/',document_list),
    path('documents-serializer/',document_list_using_Serializer),
    path('document/add',add_document)
]