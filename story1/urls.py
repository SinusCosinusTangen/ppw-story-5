from django.urls import path

from . import views

app_name = 'story1'

urlpatterns = [
    path('story1/', views.story1, name='story1'),
]