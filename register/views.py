from django.shortcuts import render
from django.contrib.auth.models import User


def register(request):
    if request.method == "GET":
        return render(request, 'register/register.html')

    username = request.POST.get('username')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    user = User.objects.filter(username=username).first()

    if user:
        return render(request, 'register/register.html', {'usuario_existe': True})

    user = User.objects.create_user(username=username, email=email, password=senha)
    user.save()

    return render(request, 'login/login.html')
