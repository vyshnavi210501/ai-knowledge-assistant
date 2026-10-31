from .models import Document
from rest_framework import serializers

class DocumentSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(
    source="owner.username",
    read_only=True
)
    class Meta:
        model = Document
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at','id','owner']  # Make 'created_at' and 'updated_at' read-only
