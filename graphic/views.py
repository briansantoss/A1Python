from django.shortcuts import render

# Create your views here.
def graphic(request):
    return render(request, 'graphic/graphic.html')