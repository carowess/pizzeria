from django.urls import path

from . import views

app_name = 'pizzas'

urlpatterns = [
    path('',views.index, name='index'), #default page
    path('pizzas',views.pizzas, name='pizzas'),
]