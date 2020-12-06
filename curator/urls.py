from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('book/', views.book, name="book"),
    path('movie/', views.movie, name="movie"),
    path('album/', views.album, name="album"),
    path('update/', views.update_collection, name="update"),
    path('delete/', views.delete_collection, name="delete"),
]