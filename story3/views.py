from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'story3/index.html')

def interest(request):
    return render(request, 'story3/interest.html')

def aboutme(request):
    return render(request, 'story3/aboutme.html')

def gallery(request):
    return render(request, 'story3/gallery.html')

def credits(request):
    return render(request, 'story3/credits.html')