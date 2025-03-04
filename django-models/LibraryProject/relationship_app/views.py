# relationship_app/views.py
from django.shortcuts import render
from .models import Book, Library  # Ensure that Library model is imported
from .models import Library
from django.views.generic.detail import DetailView
# Function-based view to list all books and their authors
def list_books(request):
    # Retrieve all books from the database
    books = Book.objects.all()

    # Render the template and pass the books as context
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for displaying library details along with books in that library
class LibraryDetailView(DetailView):
    model = Library  # This tells Django to use the Library model
    template_name = "relationship_app/library_detail.html"  # Path to the template for the library detail page
    context_object_name = "library"  # This is the context variable passed to the template