from django.urls import path
from .views import HomeView, VideoDetailView, VideoListView
app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('video/', VideoListView.as_view(), name='video'),
    path('video/detail/', VideoDetailView.as_view(), name='detail'),
]