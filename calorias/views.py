from django.shortcuts import render
from .models import Food

def index(request):
    foods = Food.objects.all()
    context = {'foods': foods}
    return render(request, 'calorias/index.html',context)



