from django.shortcuts import render


def home(request):
    return render(request, 'digiTech/home.html')


def handler_404(request):
    return render(request, 'digiTech/404.html')


def registration(request):
    return render(request, 'digiTech/registration.html')


def login(request):
    return render(request, 'digiTech/login.html')


def password_reset(request):
    return render(request, 'digiTech/password_reset.html')

def checkout(request):
    return render(request, 'digiTech/checkout.html')

