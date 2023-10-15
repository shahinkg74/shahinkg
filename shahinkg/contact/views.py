from django.shortcuts import render
from .models import tamasbama


def contact(request):
    all = tamasbama.objects.all()
    return render(request, 'contact.html', {'all': all})
