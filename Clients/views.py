from django.shortcuts import render

def index(request):
    print("uosij")
    return render(request, 'index.html')
