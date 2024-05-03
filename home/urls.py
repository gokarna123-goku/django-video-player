from django.urls import path
from .views import HomeView, VideoDetailsView, VideoListView
app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('video/', VideoListView.as_view(), name='video'),
    path('video/detail/', VideoDetailsView.as_view(), name='detail'),
]