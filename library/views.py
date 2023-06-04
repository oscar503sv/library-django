from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from .models import Libro, Prestamo, Autor
from library.forms import LoginForm

# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')

class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('libros')  # Redirige a la página después del inicio de sesión exitoso
            else:
                form.add_error(None, 'Invalid username or password.')

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')  # Redirige a la página de inicio de sesión después del logout

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')

class LibrosView(View):
    def get(self, request, *args, **kwargs):
        libros = Libro.objects.all().prefetch_related('autor_id','genero_id')
        #contexto = {'libros': libros} Se puede hacer esto y mandar el contexto al template
        return render(request,'books/books.html',{'libros':libros})

class PrestamosView(View):
    def get(self, request, *args, **kwargs):
        prestamos = Prestamo.objects.all()
        return render(request,'loans/lendout.html',{'prestamos':prestamos})

class AutoresView(View):
    def get(self, request, *args, **kwargs):
        autores = Autor.objects.all()
        return render(request,'author/authors.html',{'autores':autores})
