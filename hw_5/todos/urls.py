from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home_view, name='home'),  # Главная страница
    path('login/', views.login_page, name='login'),
    path('login/auth/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout'),
    path('todos/', views.todos_list, name='todos_list'),
    path('todos/<int:todo_id>/', views.todo_detail, name='todo_detail'),
    path('todos/add/', views.add_todo, name='add_todo'),
    path('todos/<int:todo_id>/delete/', views.delete_todo, name='delete_todo'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
     path('login/', LoginView.as_view(template_name='todos/login.html'), name='login'),
]
