from django.shortcuts import render
from django.http import HttpResponse
from matplotlib.pyplot import title

posts = [
    {
        'author': 'Michał',
        'title': 'Blog post 1',
        'content': 'Fisrt post content',
        'date_posted': '16.03.2022'
    },
    {
        'author': 'Tomek',
        'title': 'Blog post 2',
        'content': 'Fisrt post content',
        'date_posted': '16.03.2022'
    }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
