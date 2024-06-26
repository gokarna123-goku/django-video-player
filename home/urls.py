from django.urls import path
from .views import HomeView, VideoDetailView, VideoListView, SearchView, LikeView, DislikeView, LikedVideosView, FilterView
app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('video/', VideoListView.as_view(), name='video'),
    path('video/detail/<int:pk>', VideoDetailView.as_view(), name='detail'),
    path('search/', SearchView.as_view(), name='search'),
    path('like/<int:pk>/', LikeView.as_view(), name='like'),
    path('dislike/<int:pk>/', DislikeView.as_view(), name='dislike'),
    path('likedvideos/', LikedVideosView.as_view(), name='likedvideos'),
    path('filter/<str:genre>/', FilterView.as_view(), name='filter'),
]