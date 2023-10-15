from django.shortcuts import render
from .models import Blog


# Create your views here.


def blog(request):
    all = Blog.objects.all()
    return render(request, 'blog.html', {'all': all})
