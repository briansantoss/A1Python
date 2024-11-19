from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django


def login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return render(request, 'datapanel/datapanel.html')
        else:
            return render(request, 'login/login.html', {'erro_login': True})


