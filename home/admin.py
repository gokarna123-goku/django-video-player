from django.contrib import admin

# Register your models here.
from .models import Video, Comment 

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'uploaded_at')
    search_fields = ['title', 'publisher__username']
    list_filter = ['uploaded_at']
    inlines = [CommentInline]

admin.site.register(Video, VideoAdmin)
