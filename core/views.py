from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Document
from .document_serializer import DocumentSerializer

# Create your views here.

@api_view(['GET'])
def hello(request):
    print(request.path)
    print(request.method)
    return Response({"message": "AI Knowledge Assistant API is running"})

@api_view(['GET'])
def health(request):
    return Response({"status": "healthy"})

"""
this function retrieves a list of all documents from the database and returns
them as a JSON response. Each document is represented as a dictionary containing its id, 
title, and content.
"""
@api_view(['GET'])
def document_list(request):
    documents = Document.objects.all()
    document_data = [{"id": doc.id, "title": doc.title, "content": doc.content} for doc in documents]
    return Response(document_data)


"""
if we dont want to use for loop and mention all fields explicity we can use serializers to convert
 the model instances to JSON format.
"""
@api_view(['GET'])
def document_list_using_Serializer(request):
    documents = Document.objects.all()
    serializer = DocumentSerializer(documents, many=True)
    return Response(serializer.data)

"""
add document to the database using serializer. we can use POST method to add document to the database.
"""
@api_view(['POST'])
def add_document(request):
    serializer = DocumentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)