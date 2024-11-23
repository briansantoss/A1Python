from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def register(request):
    if request.method == "GET":
        return render(request, 'register/register.html')

    # Capturando dados do usuário preenchidos no formulário
    username = request.POST.get('username')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    user = User.objects.filter(username=username).first()

    if user:
        return render(request, 'register/register.html', {'usuario_existe': True})

    # Inserindo e salvando o usuário no banco de dados
    user = User.objects.create_user(username=username, email=email, password=senha)
    user.save()

    return redirect('login')
