from django.shortcuts import render

# Create your views here.
def inicioLoja(request):
    return render(request, "index.html")
def inicioLoja2(request):
    return render(request, "index2.html")