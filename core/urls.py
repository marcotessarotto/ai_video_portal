from django.urls import path
from . import views as mv


urlpatterns = [
    path('home', mv.home, name='home'),
]

