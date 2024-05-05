from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from random import choice

from .forms import VideoUploadForm
from .models import Video, Comment
from django.core.files.storage import FileSystemStorage

# Create your views here.



class HomeView(TemplateView):
    template_name = "home/index.html"

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Video, pk=pk)

        # """
        # Retrieves the context data for the current view.

        # Args:
        #     **kwargs: Additional keyword arguments.

        # Returns:
        #     dict: The context data containing the following keys:
        #         - 'video_src' (str): The URL of the randomly selected video file.
        #         - 'title' (str): The title of the selected video.
        #         - 'description' (str): The description of the selected video.

        # This method retrieves all the video objects from the Video model and selects a random video. It then sets the
        # 'video_src', 'title', and 'description' keys in the context dictionary with the corresponding values from the
        # selected video object. The 'video_id' key is commented out and not set in the context.

        # Note: The 'video_src' key is currently commented out and not set in the context.

        # Note: The 'pk' value from the kwargs is not used in this method.

        # Note: The 'videos' queryset is not used in this method and is replaced with a call to Video.objects.all().

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        videos = Video.objects.all()  # replace with your actual queryset
        # videos = Video.objects.all()  # Assuming Video model has fields 'title', 'description', and 'file'
        # context['video_src'] = choice(videos).video_file.url
        # pk = self.kwargs.get('pk')
        # print(pk)
        selected_video = choice(videos)
        # context['video_id'] = selected_video.pk
        # print(context['video_id'])
        context['video_src'] = selected_video.video_file.url
        context['title'] = selected_video.title
        context['description'] = selected_video.description
        return context
    


class VideoListView(ListView):
    model = Video
    template_name = 'videos/video.html'
    context_object_name = 'videos'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['video-active'] = 'active'
        return context


# Details page of video
class VideoDetailView(DetailView):
    template_name = "videos/detail.html"
    model = Video
    context_object_name = 'video'


    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Video, pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['video-active'] = 'active'
        return context