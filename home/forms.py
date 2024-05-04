from django import forms
from .models import Video

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file', 'video_thumbnail', 'description']

    def clean_video_file(self):
        video_file = self.cleaned_data['video_file']
        # Check if the file size is too large or if it's not a video file
        if video_file.size > 1024 * 1024 * 100:  # 100 MB
            raise forms.ValidationError("Video file is too large (max size is 100 MB)")
        if not video_file.name.endswith('.mp4'):  # Ensure it's an mp4 file
            raise forms.ValidationError("Only MP4 files are allowed")
        return video_file
