from django.shortcuts import render
from .models import HeaderTitle


def home(request):
    title = HeaderTitle.objects.all()
    return render(request, 'home.html', {'title': title})
