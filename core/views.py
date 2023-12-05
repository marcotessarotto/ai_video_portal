from django.shortcuts import render
from .models import Video, Category
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})


def video_list(request, category_id):
    videos = Video.objects.filter(category_id=category_id)
    return render(request, 'video_list.html', {'videos': videos})


def video_detail(request, video_id):
    video = Video.objects.get(id=video_id)
    return render(request, 'video_detail.html', {'video': video})


def search(request):
    query = request.GET.get('q')
    if query:
        videos = Video.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(transcript__content__icontains=query)
        )
    else:
        videos = Video.objects.none()
    return render(request, 'search_results.html', {'videos': videos})


@login_required
def user_videos(request):
    videos = Video.objects.filter(uploaded_by=request.user)
    return render(request, 'user_videos.html', {'videos': videos})
