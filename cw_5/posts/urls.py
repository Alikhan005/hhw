from django.urls import path
from . import views
from posts import views
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_page, name='login'),
    path('login/', views.login_user, name='login_post'),
    path('logout/', views.logout_user, name='logout'),
    path('posts/', views.posts_list, name='posts'),
    path('posts/my', views.my_posts, name='my_posts'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('posts/create/', views.create_post, name='create_post'),
    path('posts/<int:id>/delete/', views.delete_post, name='delete_post'),
]
