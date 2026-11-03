from .models import Document
from rest_framework import serializers
import os
from pypdf import PdfReader
from django.utils import timezone

class DocumentSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(
        source="owner.username",
        read_only=True
    )

    class Meta:
        model = Document
        fields = "__all__"
        read_only_fields = [
            "created_at",
            "updated_at",
            "id",
            "owner",
            "original_filename",
            "file_size",
            "file_type",
            "uploaded_at",
        ]

    def validate_file(self, uploaded_file):
        # 1. Check file size (5 MB)
        max_size = 5 * 1024 * 1024

        if uploaded_file.size > max_size:
            raise serializers.ValidationError(
                "File size cannot exceed 5 MB."
            )

        # 2. Check extension
        extension = os.path.splitext(uploaded_file.name)[1].lower()

        if extension not in [".pdf", ".txt"]:
            raise serializers.ValidationError(
                "Only PDF and TXT files are supported."
            )

        # 3. Validate actual file content
        try:
            if extension == ".pdf":
                if not uploaded_file.read(5).startswith(b"%PDF-"):
                    raise serializers.ValidationError(
                        "Invalid PDF file."
                    )

                uploaded_file.seek(0)
                PdfReader(uploaded_file, strict=True)

            elif extension == ".txt":
                uploaded_file.seek(0)
                uploaded_file.read().decode("utf-8")

        except serializers.ValidationError:
            raise

        except Exception:
            raise serializers.ValidationError(
                "File content is invalid or corrupted."
            )

        finally:
            uploaded_file.seek(0)

        return uploaded_file
    def create(self, validated_data):
        uploaded_file = validated_data.get("file")

        if uploaded_file:
            validated_data["original_filename"] = uploaded_file.name
            validated_data["file_size"] = uploaded_file.size
            validated_data["file_type"] = os.path.splitext(
                uploaded_file.name
            )[1].lower()
            validated_data["uploaded_at"] = timezone.now()

        return super().create(validated_data)