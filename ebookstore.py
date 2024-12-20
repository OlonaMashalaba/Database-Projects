import sqlite3

# Connect to the database or create it if it doesn't exist
conn = sqlite3.connect('ebookstore.db')
cursor = conn.cursor()

# Create the 'book' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        qty INTEGER
    )
''')

# Insert default values into the 'book' table
cursor.execute(''' 
    INSERT OR IGNORE INTO book (id, title, author, qty)
    VALUES 
    (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
    (3002, 'Harry Potter and the Philosopher''s Stone', 'J.K. Rowling', 40),
    (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
    (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
    (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
''')

# Commit the transaction
conn.commit()

# Function to add a new book
def enter_book():
    id = int(input("Enter book ID: "))
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    qty = int(input("Enter quantity: "))
    
    cursor.execute("INSERT INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)", (id, title, author, qty))
    conn.commit()
    print("Book added successfully!")

# Function to update book information
def update_book():
    id = int(input("Enter the ID of the book you want to update: "))
    title = input("Enter the new title: ")
    author = input("Enter the new author: ")
    qty = int(input("Enter the new quantity: "))
    
    cursor.execute("UPDATE book SET title = ?, author = ?, qty = ? WHERE id = ?", (title, author, qty, id))
    conn.commit()
    print("Book updated successfully!")

# Function to delete a book
def delete_book():
    id = int(input("Enter the ID of the book you want to delete: "))
    
    cursor.execute("DELETE FROM book WHERE id = ?", (id,))
    conn.commit()
    print("Book deleted successfully!")

# Function to search for a book
def search_books():
    id = int(input("Enter the ID of the book you are searching for: "))
    
    cursor.execute("SELECT * FROM book WHERE id = ?", (id,))
    book = cursor.fetchone()
    
    if book:
        print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Quantity: {book[3]}")
    else:
        print("Book not found.")

# Function to display the menu and handle user input
def menu():
    while True:
        print("\nMenu:")
        print("1. Enter book")
        print("2. Update book")
        print("3. Delete book")
        print("4. Search books")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            enter_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            search_books()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Call the menu function to start the program
menu()

# Close the connection to the database
conn.close()
