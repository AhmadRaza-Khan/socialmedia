from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('dashboard/', views.dashboard, name='dashboard' ),
    path('upload_post/', views.upload_post, name='upload_post'),
    path('get_posts/<str:username>/', views.user_posts, name='user_posts'),
    path('post/<int:post_id>/', views.like_post, name='like_post'),
    path('like_post/<str:title>/', views.like_post_one, name='like_post_one'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('update_post/<int:post_id>/', views.update_post, name='update_post'),
]
