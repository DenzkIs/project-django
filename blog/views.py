from django.shortcuts import render
from blog.models import Post
# from django.http import HttpResponse
#
# # Create your views here.
# def home(request):  # (1) функция-обработчик эндпоинта (вьюшка)
#     return HttpResponse('<h1>Hello world</h1>')
#
# def about(request):
#     return HttpResponse('<h1>Blog about</h1>')

# возвращаем теперь не HttpResponse, а render, чтобы воспользоваться html-шаблоном

# posts = [
#     {
#         'author': 'Max',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'Feb 25, 2022',
#     },
#     {
#         'author': 'Ian',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'Feb 23, 2022',
#     },
# ]

def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(
        request,
        'blog/about.html',
        {'title': 'About'}
    )
