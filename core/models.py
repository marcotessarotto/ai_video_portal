import time
from django.db import models
from django.contrib.auth.models import User


def get_directory_path(instance, filename):
    now_ms = int(time.time_ns() / 1000)
    return f"{now_ms}/{filename}"


class Category(models.Model):
    """Category model represents different categories that videos can belong to"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Transcript(models.Model):
    """Transcript model contains the text of the video transcripts"""
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Transcript {self.id}"


class Video(models.Model):
    """Video model contains details about the video, a link to its category, its transcript,
    and the user who uploaded it"""
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video_file = models.FileField(upload_to=get_directory_path)
    duration = models.DurationField(help_text="Duration of the video in seconds")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    transcript = models.OneToOneField(Transcript, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
