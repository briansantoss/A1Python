from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='login')
def data_panel(request):
    if request.method == 'GET':
        return render(request, 'data_panel/data_panel.html')
