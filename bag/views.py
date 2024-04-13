from django.shortcuts import render

# Create your views here.



def view_bag(request):
    '''
    Function to render bag content

    '''
    
    return render(request, 'bag/bag.html')