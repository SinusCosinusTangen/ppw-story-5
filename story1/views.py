from django.shortcuts import render

# Create your views here.
def story1(request):
    return render(request, 'story1/story1.html')