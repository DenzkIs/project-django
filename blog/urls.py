from django.urls import path
from blog import views # чтобы видеть функцию home
from blog.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    # (2) Тут мы добавляем новый маршрут (пустой путь) и указывам обработчиком views.home
    path('', PostListView.as_view(), name='blog-home'),  # blog-home - имя маршрута
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # blog-home - имя маршрута
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path('about/', views.about, name='blog-about')
]