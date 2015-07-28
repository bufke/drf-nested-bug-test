from rest_framework import viewsets
from .models import BookSnippet
from .serializers import BookSnippetSerializer


class BookSnippetViewSet(viewsets.ModelViewSet):
    queryset = BookSnippet.objects.all()
    serializer_class = BookSnippetSerializer
