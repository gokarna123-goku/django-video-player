from django.urls import path
from .views import RegisterView, UserLoginView, UserProfileView, UserLogoutView, UserActivityView
app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('liked_videos/', UserActivityView.as_view(), name='liked_videos'),
]