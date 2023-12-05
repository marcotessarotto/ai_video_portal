from django.urls import path
from . import views as mv


urlpatterns = [
    path('home/', mv.home, name='home'),
    path('video_list/<int:category_id>/', mv.video_list, name='video_list'),
    path('video_detail/<int:video_id>/', mv.video_detail, name='video_detail'),
    path('search/', mv.search, name='search'),
]

