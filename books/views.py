from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from common.utils import PageNumberPagination

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = PageNumberPagination
