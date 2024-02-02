from . import models
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ['id', 'title', 'author', 'created_at', 'updated_at']
        read_only_fields = ('id', 'created_at', 'updated_at')
