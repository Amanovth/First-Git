from django.shortcuts import render


def register(request):
    return render(request, 'create/register.html')

def login(request):
    return render(request, 'create/login.html')