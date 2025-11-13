from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from books.serializers import BookSerializer
from books.Serivces import book_service

@api_view(['GET', 'POST'])
def book_list(request):
    try:
        if request.method == 'GET':
            books = book_service.list_book()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == 'POST':
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                new_book = book_service.create_new_book(serializer.validated_data)
                return Response(BookSerializer(new_book).data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, book_id):
    try:
        if request.method == 'GET':
            book = book_service.get_book(book_id)
            serializer = BookSerializer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                updated_book = book_service.update_existing_book(book_id, serializer.validated_data)
                return Response(BookSerializer(updated_book).data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            book_service.delete_existing_book(book_id)
            return Response({"message": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


    except ValueError as ve:
        return Response({"error": str(ve)}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
