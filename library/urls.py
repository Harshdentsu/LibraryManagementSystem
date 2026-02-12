from django.contrib import admin
from django.urls import path,include
from .views import BookListView,BookCreateView,BookUpdateView,BookDeleteView,BookExportView,BookUploadView

urlpatterns = [
    path('book_list/',BookListView.as_view()),
    path('create_book/',BookCreateView.as_view()),
    path('update_book/<int:pk>/',BookUpdateView.as_view()),
    path('delete_book/<int:pk>/',BookDeleteView.as_view()),
    path('export_books/',BookExportView.as_view()),
    path('upload_books/',BookUploadView.as_view()),
]