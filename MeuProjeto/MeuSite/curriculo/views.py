from django.shortcuts import render

# Create your views here.
def meucurriculo(request):
    return render(request, 'curriculo/meucurriculo.html')
def curriculospiff(request):
    return render(request, 'curriculo/curriculospiff.html')     