from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, CreateView, ListView

from home.models import Video

from .forms import RegisterForm
from .models import CustomUser
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login as auth_login


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


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_message = "You were successfully logged in."
    success_url = 'acounts:profile'


    def form_valid(self, form):
        user = form.get_user()
        if user.is_superuser :
            auth_login(self.request, form.get_user())
            messages.success(self.request,'Logged in as a Superuser.')
            return redirect('/admin/')
        # elif  not user.is_verified :
        #     # messages.error(self.request, "Verify Your Email First.")
        #     messages.info(self.request, "You are still under verification.")
        elif user.is_active :
            auth_login(self.request, form.get_user())
            messages.success(self.request,'Logged in successfully.')
            return redirect('accounts:profile')
        else:
            messages.error(self.request, "Something went terribly wrong.")

        # return HttpResponseRedirect(self.get_success_url())
        return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid Username or Password')
        return self.render_to_response(self.get_context_data(form=form))


# Logout View
class UserLogoutView(LogoutView):
    next_page='accounts:login'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.SUCCESS, "You have logged out. Login again.")
        return response

    def get_success_url(self):
        return reverse_lazy('accounts:login')


class UserProfileView(TemplateView):
    template_name = 'accounts/profile.html'
    model = CustomUser
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user
    

# Getting all videos that user liked

class UserActivityView(ListView):
    model = Video
    template_name = 'accounts/profile.html'
    context_object_name = 'activity'

    def get_queryset(self):
        liked_videos = self.request.user.liked_videos.all()
        print(liked_videos)
        commented_videos = self.request.user.commented_videos.all()
        print(commented_videos)
        return liked_videos | commented_videos | self.request.user.uploaded_videos.all()