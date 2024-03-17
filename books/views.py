from django.shortcuts import render
from rest_framework.views import APIView
from books.models import Book
from books.serializers import BookSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status


# Create your views here.


class BookAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book)
            return Response(
                {"status": "Success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(
            {"status": "Success", "data": serializer.data}, status=status.HTTP_200_OK
        )

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response(
                {"message": "something went worng", "errors": serializer.errors}
            )

        serializer.save()
        return Response({"messages": "success", "payload": serializer.data})

    def put(self, request, pk):
        try:
            book_obj = Book.objects.get(pk=pk)
            serializer = BookSerializer(book_obj, data=request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response(
                    {"message": "something went worng", "errors": serializer.errors}
                )

            serializer.save()
            return Response({"messages": "success", "payload": serializer.data})
        except Exception as e:
            print(e)
            return Response({"message": "invallid ID"})

    def patch(self, request, pk):
        try:
            book_obj = Book.objects.get(pk=pk)
            serializer = BookSerializer(book_obj, data=request.data, partial=True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response(
                    {"message": "something went worng", "errors": serializer.errors}
                )

            serializer.save()
            return Response({"messages": "success", "payload": serializer.data})
        except Exception as e:
            print(e)
            return Response({"message": "invallid ID"})

    def delete(self, request, pk):
        try:

            book_obj = Book.objects.get(pk=pk)
            return Response({"message": "deleted success"})
        except Exception as e:
            print(e)
            return Response({"message": "invallid ID"})

    def delete(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response({"message": "Deleted"})
