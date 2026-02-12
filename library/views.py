import csv
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class BookListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        books=Book.objects.all()
        serializer=BookSerializer(books,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class BookCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors)

class BookUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request,pk):
        book=Book.objects.get(pk=pk)
        serializer=BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors)

class BookDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self,request,pk):
        book=Book.objects.get(pk=pk)
        book.delete()
        return Response({"Deleted Successfully"},
                        status=status.HTTP_204_NO_CONTENT)

class BookExportView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self ,request):
        books=Book.objects.all()
        file = HttpResponse(content_type='text/csv')
        file['Content-Disposition'] = 'attachment; filename="books.csv"'
        writer = csv.writer(file)
        writer.writerow(['title', 'author', 'genre','publication_year'])
        for book in books:
            writer.writerow([book.title, book.author, book.genre,book.publication_year])
        return file
       
class BookUploadView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def post(self, request):
        file = request.FILES.get('file')

        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.reader(decoded_file)
        next(reader, None)  

        for row in reader:
            Book.objects.create(
                title=row[0],
                author=row[1],
                genre=row[2],
                publication_year=row[3]
            )

        return Response({'message': 'Tasks uploaded successfully'}, status=201)