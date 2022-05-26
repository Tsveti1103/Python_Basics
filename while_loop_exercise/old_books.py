anys_book = input()
book = ""
book_count = 0
while anys_book != book:
    book = input()
    if book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {book_count} books.")
        break
    if anys_book == book:
        print(f"You checked {book_count} books and found it.")
    book_count += 1