from .models import Book
from rest_framework import viewsets
from rest_framework import generics
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = self.queryset
        author_filter = self.request.query_params.get('author', None)
        if author_filter is not None:
            queryset = queryset.filter(author__icontains=author_filter)    
        return queryset