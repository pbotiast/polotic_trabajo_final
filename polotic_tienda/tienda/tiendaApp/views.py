from django.shortcuts import render
from .models import *




def acercade(request):

    return render(request, 'tiendaApp/acercade.html')

