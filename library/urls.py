from django.urls import path
from .views import render_libros

urlpatterns = [
    path('books/', render_libros, name='libros')
]