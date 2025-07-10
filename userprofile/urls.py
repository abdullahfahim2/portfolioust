from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('',home,name='home'),
    path('blogs/<slug:slug>',blog_details,name='blogdetails'),
    path('image-gallery/',imagegallery,name='image'),
    path('video-gallery/',videogallery,name='video'),
    path('service/<int:pk>',service,name='service'),
    path('download-cv/<int:pk>/', download_cv, name='download_cv'),
]