from django.shortcuts import render

# Create your views here.


def helloworld(request):
    return render(request, "posts/artwork.html")


def index(request):
    return render(request, "base.html")
