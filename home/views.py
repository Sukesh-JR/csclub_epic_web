from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def team(request):
    return render(request, 'home/team.html')

def contact(request):
    return render(request, 'home/contact.html')

def timeline(request):
    return render(request, 'home/timeline.html')

def event(request):
    return render(request, 'home/events.html')