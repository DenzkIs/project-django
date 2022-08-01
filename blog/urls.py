from django.urls import path
from blog import views # чтобы видеть функцию home


urlpatterns = [
    # (2) Тут мы добавляем новый маршрут (пустой путь) и указывам обработчиком views.home
    path('', views.home, name='blog-home'),  # blog-home - имя маршрута
    path('about/', views.about, name='blog-about')  # blog-home - имя маршрута
]