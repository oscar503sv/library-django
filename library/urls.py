from django.urls import path
from .views import LibrosView, PrestamosView, AutoresView

urlpatterns = [
    path('books/', LibrosView.as_view(), name='libros'),
    path('lendout/', PrestamosView.as_view(), name='prestamos'),
    path('authors/',AutoresView.as_view(),name='autores')
]