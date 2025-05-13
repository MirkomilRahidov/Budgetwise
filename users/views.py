from django.shortcuts import render,redirect
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import RegisterForm,LoginForm,ProfileUpdateForm
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'auth/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('card_list')
        return render(request, 'auth/register.html', {'form': form})
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'auth/login.html', {'form': form})
    def post(self, request):
        form =LoginForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            password = form.cleaned_data['password']
            user= authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('card_list')
            return render(request,'auth/login.html', {'form':form})
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('card_list')
class ProfileView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        form = ProfileUpdateForm(instance=request.user)

        return render(request, 'auth/profile.html', {
            'form': form,
        })
@login_required
def profileupdate(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:=profile')  
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, "auth/profile_update.html", {"form": form})