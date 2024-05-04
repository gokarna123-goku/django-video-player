from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, CreateView
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, LoginForm
from .models import User
from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth.views import LogoutView


class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    # success_url = 'accounts:login'

    def form_valid(self, form):
        form.save()
        # email = form.cleaned_data.get('email')
        # password = form.cleaned_data.get('password1')
        # user = authenticate(email=email, password=password)
        # login(self.request, user)
        messages.success(self.request, 'Successfully Created Your Account!')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('accounts:login')



class LoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, email=email, password=password)
        print(user)
        if user is not None:
            login(self.request, user)
            messages.success(self.request, 'Successfully Created Your Account!')
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Invalid email or password')
            return self.form_invalid(form)
        
    def get_success_url(self):
        return reverse_lazy('accounts:profile')
    


# Logout View
class UserLogoutView(LogoutView):
    # http_method_names = ['post', 'get']
    next_page='home:home'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.SUCCESS, "You have logged out successfully, thank you for using our service.")
        return response
    
    def get_success_url(self):
        return reverse_lazy('accounts:login')



class UserProfileView(TemplateView):
    template_name = 'accounts/profile.html'
    model = User
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user
    

class VideoUploadView(TemplateView):
    template_name = 'uploadvideo/upload.html'
    model = User
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user
    
