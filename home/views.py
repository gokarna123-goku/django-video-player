from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = "home/index.html"
    

class VideoListView(TemplateView):
    template_name = "videos/video.html"


# Details page of video
class VideoDetailsView(TemplateView):
    template_name = "videos/detail.html"