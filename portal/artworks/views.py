from django.shortcuts import render

# Create your views here.


def helloworld(request):
    return render(request, "posts/artwork.html")
