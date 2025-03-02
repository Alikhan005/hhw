from django.contrib import admin
from django.urls import path, include
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Добавляем главную страницу
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('posts/', include('posts.urls')),  # Включаем маршруты приложения posts
]
