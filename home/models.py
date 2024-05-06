from django.db import models

from accounts.models import CustomUser

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
    video_thumbnail = models.ImageField(upload_to='thumbnails/')
    description = models.TextField()
    publisher = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    @property
    def comments(self):
        return VideoComment.objects.filter(video=self)



class VideoComment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"Comment by {self.user.email} on {self.video.title}"
    
