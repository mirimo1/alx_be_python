# oop/main.py

from book_class import Book
from library_system import Book as LibBook, EBook, PrintBook, Library

def run_book_class_task():
    print("\n=== Running Book Class Task ===")
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)        # __str__
    print(repr(my_book))  # __repr__
    del my_book           # __del__

def run_library_system_task():
    print("\n=== Running Library System Task ===")
    my_library = Library()

    classic_book = LibBook("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    my_library.list_books()

if __name__ == "__main__":
    # Run both tasks in sequence
    run_book_class_task()
    run_library_system_task()
