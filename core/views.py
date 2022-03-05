
from django.shortcuts import render



def hello(request):
    return render(request, 'core/hello.html', {'name':'vasya'})

