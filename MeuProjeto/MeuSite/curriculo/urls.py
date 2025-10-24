from django.urls import path    
from . import views

app_name = 'curriculo'

urlpatterns = [
    path('meucurriculo/', views.meucurriculo, name='meucurriculo'),
    path('curriculospiff/', views.curriculospiff, name='curriculospiff'),
]