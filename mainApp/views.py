from django.shortcuts import render

def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['Если у вас '
    'остались вопросы, то задавайте их мне по телефону', '(123) 456-78-90']})

def index(request):
    return render(request, 'mainApp/homePage.html')
