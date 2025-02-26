from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)  # Retrieve the author by name
    books = Book.objects.filter(author=author)  # Filter books by author
    for book in books:
        print(book.title)

# 2. List all books in a specific library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)  # Retrieve the library by name
    books = library.books.all()  # Retrieve all books in that library
    for book in books:
        print(book.title)

# 3. Retrieve the librarian for a specific library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)  # Retrieve the library by name
    librarian = Librarian.objects.get(library=library)  # Retrieve the librarian associated with the library
    print(librarian.name)

# Test the queries by calling them
if __name__ == "__main__":
    # Example: Get all books by an author named 'J.K. Rowling'
    print("Books by J.K. Rowling:")
    books_by_author("J.K. Rowling")

    # Example: Get all books in a library named 'Central Library'
    print("\nBooks in Central Library:")
    books_in_library("Central Library")

    # Example: Get the librarian for a library named 'Central Library'
    print("\nLibrarian for Central Library:")
    librarian_for_library("Central Library")