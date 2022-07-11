from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model
from django.contrib.auth import logout, authenticate, login

from .forms import RegistrationForm

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        template_name = 'registration/login.html'
        if user is not None:
            login(request, user)
            return redirect('todos')
        else:
            return redirect('landing')
    else:
        return render(request, 'registration/login.html')

def logout_user(request):
    logout(request)
    return redirect('landing')

class RegisterView(FormView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()  # save the user
        return super().form_valid(form)


# htmx views 

def check_username(request):
    username = request.POST.get('username')
 
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse('<div id="username-error" class="error">This username already exists!</div>')
    return HttpResponse('<div id="username-error" class=" success">This username is available!</div>')