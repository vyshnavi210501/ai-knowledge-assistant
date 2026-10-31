from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .models import Document
from .document_serializer import DocumentSerializer
from rest_framework.permissions import IsAuthenticated
from .DocumentPagination import DocumentPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

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
class DocumentListView(ListAPIView):
    """View to list all documents for the authenticated user with pagination, search, and ordering support.updated this get apiview to use 
    ListAPIView which is a generic view that provides built-in support for listing objects and handling pagination, filtering, and ordering."""

    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    pagination_class = DocumentPagination

    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend]

    search_fields = ['title', 'content']

    ordering_fields = ['title', 'created_at']
    filterset_fields = {
    'created_at': ['date__exact', 'date__gte', 'date__lte']
}
    def get_queryset(self):
        return Document.objects.filter(owner=self.request.user)


"""
if we dont want to use for loop and mention all fields explicity we can use serializers to convert
 the model instances to JSON format.
"""
@api_view(['GET',"POST",'PUT','DELETE','PATCH'])
@permission_classes([IsAuthenticated])
def document_list_using_Serializer(request,pk=None):
    if request.method == 'PUT':
        try:
            document = Document.objects.get(pk=pk,owner=request.user)
        except Document.DoesNotExist:
            return Response({"error": "Document not found"}, status=404)

        serializer = DocumentSerializer(document, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Set the owner to the authenticated user",stat})
            return Response({"message": "Document updated successfully"},status=204)
        return Response(serializer.errors, status=400)
    elif request.method=='DELETE':
        try:
            document=Document.objects.get(pk=pk,owner=request.user)
            document.delete()
            return Response({"message": "Document deleted successfully"},status=204)
        except Document.DoesNotExist:
            return Response({"error": "Document not found"}, status=404)
    elif request.method=='PATCH':
        try:
            document=Document.objects.get(pk=pk,owner=request.user)
            serializer = DocumentSerializer(document, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Document.DoesNotExist:
            return Response({"error": "Document not found"}, status=404)
    document = Document.objects.get(pk=pk,owner=request.user)
    serializer = DocumentSerializer(document)
    return Response(serializer.data)

"""
add document to the database using serializer. we can use POST method to add document to the database.
"""
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_document(request):
    serializer = DocumentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)  # Set the owner to the authenticated user
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)