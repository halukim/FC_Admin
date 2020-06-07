from django.views import generic
from django.shortcuts import render


def IndexView(request):
    return render(request, 'report/index.html')