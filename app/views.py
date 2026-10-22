from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def kt2(request):
    return render(request, 'kt2.html')


def kt3(request):
    return render(request, 'kt3.html')

def kt4(request):
    return render(request, 'kt4.html')