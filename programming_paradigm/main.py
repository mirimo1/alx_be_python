import sys
from robust_division_calculator import safe_divide
from library_management import Book, Library

def run_division(args):
    if len(args) != 2:
        print("Usage for division: python main.py divide <numerator> <denominator>")
        return
    numerator, denominator = args
    result = safe_divide(numerator, denominator)
    print(result)

def run_library():
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    print("Available books after setup:")
    library.list_available_books()

    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print(" python main.py divide <numerator> <denominator>")
        print(" python main.py library")
        sys.exit(1)

    command = sys.argv[1]

    if command == "divide":
        run_division(sys.argv[2:])
    elif command == "library":
        run_library()
    else:
        print("Unknown command. Use 'divide' or 'library'.")

if __name__ == "__main__":
    main()
