from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, TemplateView
from random import choice
from django.contrib.auth.decorators import login_required

from django.db.models import Q 

from .models import Video

from .forms import CommentForm


# Create your views here.

class HomeView(TemplateView):
    template_name = "home/index.html"

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Video, pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        videos = Video.objects.all()
        if len(videos) > 0:
            selected_video = choice(videos)
            context['video_src'] = selected_video.video_file.url
            context['title'] = selected_video.title
            context['description'] = selected_video.description
            return context
        else:
            # display default videos
            context['video_src'] = '../static/video/video1.mp4'
            context['title'] = "The Amazing Waterfall in the worlds"
            context['description'] = "This is the default video. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
            return context

    # def get_recent_videos(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     recent_videos = Video.objects.all().order_by('uploaded_at')
    #     context['recent_videos'] = recent_videos  # Update the key to 'recent_videos'
    #     return context


    def get_recent_videos(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recent_videos = Video.objects.all().order_by('uploaded_at')
        context['recent_videos'] = recent_videos
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
        context['form'] = CommentForm()
        # context['title'] = Video.objects.filter(user=self.request.user, title=context['title']).first()
        return context
    
    def post(self, request, *args, **kwargs):
        video = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.video = video
            comment.user = request.user
            comment.save()
            # messages.success(request, 'Comment posted.')
            return HttpResponseRedirect(self.request.path_info +'#comments')
        else:
            messages.error(request, 'Something went wrong.')
            return HttpResponseRedirect(self.request.path_info +'#comments')

    

class SearchView(ListView):
    model = Video
    template_name = 'search/search.html'
    
    def get(self, request, *args, **kwargs):
        search_result = request.GET.get('search')
        # if search_result:
        #     search_videos = Video.objects.filter(Q(title__icontains=search_result) | Q(producer__icontains=search_result) | Q(genre__icontains=search_result))
        if search_result:
            search_videos = Video.objects.filter(
            Q(title__icontains=search_result) |
            Q(producer__icontains=search_result)
            )
        else:
            print("Sorry, no results founds")
        context = {
            'search_videos': search_videos,
        }
        return render(request, self.template_name, context)
