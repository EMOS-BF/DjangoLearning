from django.shortcuts import render

# Create your views here.
from .models import Pizza
# Create your views here.
def index(request):
    Pizzas = Pizza.objects.all().order_by("prix")
    """Pizzas_names =[Pizza.nom + " : "+ str(Pizza.prix) + "£" for Pizza in Pizzas]
    Pizzas_names_str= ", ".join(Pizzas_names)"""
    return render(request, 'menu/index.html', {"Pizzas": Pizzas})