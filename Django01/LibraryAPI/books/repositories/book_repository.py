from books.models import Book

def get_all_books():
    return Book.objects.all()

def get_book_by_id(book_id):
    try:
        return Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return None

def create_book(data):
    return Book.objects.create(**data)

def update_book(book, data):
    for key, value in data.items():
        setattr(book, key, value)
    book.save()
    return book

def delete_book(book):
    book.delete()