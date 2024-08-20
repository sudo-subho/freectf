from django.shortcuts import render

def room(request):
    return render(request, 'room.html', {})

def room2(request):
    return render(request, 'room2.html', {})
def room3(request):
    return render(request, 'room3.html', {})

def room4(request):
    return render(request, 'room4.html', {})

def home(request):
    return render(request, 'home.html', {})

