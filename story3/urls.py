from django.urls import path

from . import views

app_name = 'story3'

urlpatterns = [
    path('', views.index, name='index'),
    path('interest/', views.interest, name='interest'),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('gallery/', views.gallery, name='gallery'),
    path('credits/', views.credits, name='credits'),
]