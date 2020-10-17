from form_story5.views import tambah
from django.urls import path

from . import views

app_name = 'story5'

urlpatterns = [
    path('story5/', views.schedule, name='schedule'),
    path('tambah/', views.tambah, name='tambah'),
    path('update/<str:param>/', views.update, name='update'),
    path('hapus/<str:param>/', views.hapus, name='hapus'),
    path('detail/<str:param>/', views.details, name='detail')
]