from django.shortcuts import render
from .models import Portfolio


def portfolio(request):
    all = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'all': all})
