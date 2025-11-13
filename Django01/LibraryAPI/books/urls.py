from django.urls import path
from books.views import book_views

urlpatterns = [
    path('books/', book_views.book_list, name='book-list'),
    path('books/<int:book_id>/', book_views.book_detail, name='book-detail'),
]