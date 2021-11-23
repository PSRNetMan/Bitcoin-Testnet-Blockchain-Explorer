from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "myapp/home.html")

def exptest(request):
    prm = request.GET.get('anything', '')
    if prm == '':
       return HttpResponse("Tester Bester")
    else:
       return HttpResponse(prm)
