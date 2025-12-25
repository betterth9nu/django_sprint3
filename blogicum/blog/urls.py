from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Главная
    path('', views.index, name='index'),

    # Детальная страница поста
    path('posts/<int:id>/', views.post_detail, name='post_detail'),

    # Категории
    path('category/<slug:category_slug>/', views.category_posts,
         name='category_posts'),
]
