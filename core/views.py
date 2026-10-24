from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def hello(request):
    print(request.path)
    print(request.method)
    return Response({"message": "AI Knowledge Assistant API is running"})

@api_view(['GET'])
def health(request):
    return Response({"status": "healthy"})


def index(request):
    if request.method == 'GET':
        return {"message": "AI Knowledge Assistant API is running"}