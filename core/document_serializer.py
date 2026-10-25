from .models import Document
from rest_framework import serializers

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['title', 'content', 'created_at', 'updated_at','id']
        read_only_fields = ['created_at', 'updated_at']
