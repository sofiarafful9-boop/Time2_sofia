from django.shortcuts import render

def home(request):
    '''
    View function for home page of site.
    Renders the home.html template.
    '''
    return render(request, 'MeuSite/home.html')
from django.contrib.auth.decorators import login_required
@login_required
def meucurriculo(request):
    '''
    View function for the user's curriculum page.
    Renders the meucurriculo.html template.
    '''
    return render(request, 'MeuSite/meucurriculo.html')