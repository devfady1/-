# project/views.py
from django.shortcuts import render

def handle404(request, exception):
    return render(request, '404.html', status=404)

def handle500(request):
    return render(request, '500.html', status=500)
