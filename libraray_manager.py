import json

def load_library():
    try:
        with open('library.txt', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_library(library):
    with open('library.txt', 'w') as f:
        json.dump(library, f)

def add_book(library):
    print("\nAdd a New Book")
    title = input("Enter the book title: ").strip()
    while not title:
        print("Title cannot be empty.")
        title = input("Enter the book title: ").strip()
    
    author = input("Enter the author: ").strip()
    while not author:
        print("Author cannot be empty.")
        author = input("Enter the author: ").strip()
    
    while True:
        year_str = input("Enter the publication year: ").strip()
        try:
            year = int(year_str)
            if year < 0:
                print("Year must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid year. Please enter a valid integer.")
    
    genre = input("Enter the genre: ").strip()
    while not genre:
        print("Genre cannot be empty.")
        genre = input("Enter the genre: ").strip()
    
    while True:
        read_status = input("Have you read this book? (yes/no): ").strip().lower()
        if read_status in ['yes', 'y', 'no', 'n']:
            break
        print("Please enter 'yes' or 'no'.")
    
    read = read_status in ['yes', 'y']
    book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }
    library.append(book)
    print("\nBook added successfully!")

def remove_book(library):
    title = input("\nEnter the title of the book to remove: ").strip()
    initial_count = len(library)
    library[:] = [book for book in library if book['title'] != title]
    removed_count = initial_count - len(library)
    if removed_count > 0:
        print(f"\n{removed_count} book(s) removed successfully!")
    else:
        print("\nNo books found with that title.")

def search_books(library):
    print("\nSearch by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ").strip()
    
    if choice not in ['1', '2']:
        print("Invalid choice.")
        return
    
    search_term = input("Enter your search term: ").strip().lower()
    results = []
    
    if choice == '1':
        results = [book for book in library if search_term in book['title'].lower()]
    else:
        results = [book for book in library if search_term in book['author'].lower()]
    
    if not results:
        print("\nNo matching books found.")
        return
    
    print("\nMatching Books:")
    for idx, book in enumerate(results, 1):
        status = "Read" if book['read'] else "Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_books(library):
    if not library:
        print("\nYour library is empty.")
        return
    
    print("\nYour Library:")
    for idx, book in enumerate(library, 1):
        status = "Read" if book['read'] else "Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_stats(library):
    total = len(library)
    print(f"\nTotal books: {total}")
    
    if total == 0:
        return
    
    read_count = sum(book['read'] for book in library)
    percentage = (read_count / total) * 100
    print(f"Percentage read: {percentage:.1f}%")

def main():
    library = load_library()
    
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("\nEnter your choice: ").strip()
        
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_books(library)
        elif choice == '4':
            display_books(library)
        elif choice == '5':
            display_stats(library)
        elif choice == '6':
            save_library(library)
            print("\nLibrary saved to file. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1-6.")

if __name__ == "__main__":
    main()