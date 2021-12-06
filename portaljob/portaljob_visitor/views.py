from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'portaljob_visitor/index.html')

def recruitment(request):
    return render(request,'portaljob_visitor/recruitment.html')