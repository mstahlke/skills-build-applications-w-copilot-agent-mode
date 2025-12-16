from django.shortcuts import render

# Placeholder views for the tracker app
def index(request):
    return render(request, 'tracker/index.html', {})
