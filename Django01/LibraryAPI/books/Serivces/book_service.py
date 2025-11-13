from books.repositories import book_repository

def list_book():
    return book_repository.get_all_books()

def get_book(book_id):
    book = book_repository.get_book_by_id(book_id)
    if not book:
        raise ValueError("Book not found")
    return book

def create_new_book(data):
    return book_repository.create_book(data)

def update_existing_book(book_id, data):
    book = book_repository.get_book_by_id(book_id)
    if not book:
        raise ValueError("Book not found")
    return book_repository.update_book(book, data)

def delete_existing_book(book_id):
    book = book_repository.get_book_by_id(book_id)
    if not book:
        raise ValueError("Book not found")
    book_repository.delete_book(book)