from django.contrib import admin

# Register your models here.
from .models import Video, VideoComment, Genre


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'uploaded_at')
    search_fields = ['title', 'publisher__username']
    list_filter = ['uploaded_at']
    # inlines = [CommentInline]

class VideoGenreAdmin(admin.ModelAdmin):
    list_display = ('genre', 'created_at')
    search_fields = ['genre', 'created_at']
    list_filter = ['created_at']

class VideoCommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'created_at')
    search_fields = ['comment','created_at']
    list_filter = ['created_at']

admin.site.register(Video, VideoAdmin)
admin.site.register(Genre, VideoGenreAdmin)
admin.site.register(VideoComment, VideoCommentAdmin)
