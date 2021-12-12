from django.shortcuts import render

from .models import Pizza


# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')


def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added') # minus sign here if you want to do descending order
   
    context = {'pizzas':pizzas}

    return render(request, 'pizzas/pizzas.html', context)