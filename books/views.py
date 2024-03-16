from django.shortcuts import render
from rest_framework.views import APIView
from books.models import Book
from books.serializers import BookSerializer
from rest_framework.response import Response


# Create your views here.

class BookAPIView(APIView):
    def get(self,request):
        book_objs = Book.objects.all()
        serializer = BookSerializer(book_objs,many=True)
        return Response({"message": 200, "payload": serializer.data})
    def post(self,request):
        data = request.data
        serializer = BookSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response(
                {"message": "something went worng", "errors": serializer.errors}
            )

        serializer.save()
        return Response({"messages": "success", "payload": serializer.data})
    def put(self,request,pk):
        try:
            book_obj = Book.objects.get(pk=pk)
            serializer = BookSerializer(book_obj,data=request.data)

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
            book_obj.delete()
            book_obj = Book.objects.get(pk=pk)
            return Response({"message": "deleted success"})
        except Exception as e:
            print(e)
            return Response({"message": "invallid ID"})


