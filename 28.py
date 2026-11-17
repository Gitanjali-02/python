books = []

while True:
    print("\n1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        books.append(book)
        print("Book added successfully")

    elif choice == 2:
        print("Available Books:", books)

    elif choice == 3:
        book = input("Enter book name: ")
        if book in books:
            print("Book found")
        else:
            print("Book not found")

    elif choice == 4:
        break

    else:
        print("Invalid choice")