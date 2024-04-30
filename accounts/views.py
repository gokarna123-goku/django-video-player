from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, LoginForm
from .models import User


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

# Logout View
# class DLogoutView(LogoutView):
#     next_page='accounts:login'

#     def dispatch(self, request, *args, **kwargs):
#         response = super().dispatch(request, *args, **kwargs)
#         messages.add_message(request, messages.SUCCESS, "You have logged out. Login again.")
#         return response


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        email = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, email=email, password=password)
        print(user, " users")
        if user is not None:
            login(self.request, user)
            messages.success(self.request, 'Successfully Logged In!')
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Invalid email or password')
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('accounts:profile')
    

class UserProfileView(TemplateView):
    template_name = 'accounts/profile.html'
    model = User
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user
    
