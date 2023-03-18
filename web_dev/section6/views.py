from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'section6/index.html')

def bootstrap(request):
    return render(request, 'section6/bootstrappractice.html')


def tindog(request):
    return render(request, 'section6/tindog.html')