from django.shortcuts import render
from .models import Book  # Make sure the Book model is imported

# Function-based view to list all books and their authors
def list_books(request):
    # Retrieve all books from the database
    books = Book.objects.all()

    # Render the template and pass the books as context
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'