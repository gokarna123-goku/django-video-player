from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import VideoUploadForm
from .models import Video, Comment

# from django.views.generic import View
from django.core.files.storage import FileSystemStorage

# Create your views here.


class HomeView(TemplateView):
    template_name = "home/index.html"
    


class VideoListView(ListView):
    model = Video
    template_name = 'videos/video.html'
    context_object_name = 'videos'


# Details page of video
class VideoDetailView(TemplateView):
    template_name = "videos/detail.html"