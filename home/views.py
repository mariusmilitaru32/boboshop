from django.shortcuts import render



# Create your views here.

def index(request):
    """
    render index page
    """
    return render(request, 'index.html')


