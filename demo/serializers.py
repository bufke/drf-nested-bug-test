from rest_framework import serializers
from .models import Book, BookSnippet


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book


class BookSnippetSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    class Meta:
        model = BookSnippet

    def create(self, validated_data):
        print(validated_data)
