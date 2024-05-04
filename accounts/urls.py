from django.urls import path
from .views import RegisterView, LoginView, UserProfileView, VideoUploadView, UserLogoutView
app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/upload/', VideoUploadView.as_view(), name='upload'),
]