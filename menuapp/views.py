from django.shortcuts import render


def index(request, id=None):
    context = {}
    return render(request, 'index.html', context)