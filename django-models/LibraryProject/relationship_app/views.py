# relationship_app/views.py
from urllib import request
from django.shortcuts import render
from .models import Book, Library  # Ensure that Library model is imported
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
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
     # User registration view (function-based view)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Automatically log in the user after registration
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Redirect to home after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})