from django.shortcuts import render

def index(request):
    return render(request, 'bootstrapLessons/homePage.html')

# Create your views here.
