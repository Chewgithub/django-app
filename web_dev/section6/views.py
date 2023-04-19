from django.shortcuts import render
    
# Create your views here.


def index(request):
    return render(request, 'section6/index.html')

def bootstrap(request):
    return render(request, 'section6/bootstrappractice.html')


def tindog(request):
    return render(request, 'section6/tindog.html')


def dom(request):
    return render(request, 'section6/DOM.html')


def dice(request):
    return render(request, 'section6/dicee.html')

def drumroll(request):
    return render(request, 'section6/drumroll.html')

def jquery(request):
    return render(request, 'section6/jquery.html')

def simon(request):
    return render(request, 'section6/simon.html')