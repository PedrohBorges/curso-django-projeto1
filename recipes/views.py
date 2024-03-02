from django.shortcuts import render


# Create your views here.

def my_view(request):
    return render(request, 'recipes/pages/home.html')

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html')
