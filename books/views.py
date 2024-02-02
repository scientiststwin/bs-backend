from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from common.utils import PageNumberPagination
from django.db.models import Q


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()

        query = self.request.query_params.get('query', None)

        if query:
            search_query = Q(
                title__icontains=query) | Q(
                author__icontains=query)
            queryset = queryset.filter(search_query)

        return queryset
