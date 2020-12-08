from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('book/', views.book, name='book'),
    path('movie/', views.movie, name='movie'),
    path('album/', views.album, name='album'),
    path('book/delete_book/', views.delete_book, name='delete_book'),
    path('book/delete_movie/', views.delete_movie, name='delete_movie'),
    path('book/delete_album/', views.delete_album, name='delete_album'),
    path('book/new_book/', views.new_book, name='new_book'),
    path('movie/new_movie/', views.new_movie, name='new_movie'),
    path('album/new_album/', views.new_album, name='new_album')
]