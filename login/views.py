from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django


def login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')

    # Capturando dados (nome de usuário e senha) do usuário preenchidos no fórmulario
    username = request.POST.get('username')
    senha = request.POST.get('senha')

    user = authenticate(username=username, password=senha)

    if user:
        login_django(request, user)
        return redirect('data_panel')
    return render(request, 'login/login.html', {'erro_login': True})
