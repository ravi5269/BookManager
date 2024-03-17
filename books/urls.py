from django.urls import path
from books.views import BookAPIView
from django.contrib import admin

urlpatterns = [
    path("books/", BookAPIView.as_view()),
    path("book/<int:pk>", BookAPIView.as_view()),
    
    
]