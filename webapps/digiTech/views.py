from django.shortcuts import render


def home(request):
    return render(request, 'digiTech/home.html')


def handler_404(request):
    return render(request, 'digiTech/404.html')

