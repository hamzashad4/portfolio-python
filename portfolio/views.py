from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'portfolio/index.html')

def about(request):
    return render(request, 'portfolio/about.html')

def contact(request):
    return render(request, 'protfolio/contact.html')

# def base(request):
#     return render(request, 'base.html')


