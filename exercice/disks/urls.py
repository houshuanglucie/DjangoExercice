from django.urls import path
from . import views

urlpatterns = [
    path('album_list/<int;id>', views.album_list, name='album_list'),
    path('album_info/<int;id>', views.album_info, name='album_info'),
    # path(r'^search/$', views.search),
]