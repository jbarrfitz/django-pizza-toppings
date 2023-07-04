from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Topping


class ToppingsListView(ListView):
    template_name = "toppings/toppings_list.html"
    model = Topping
    context_object_name = "toppings"


class ToppingsDetailView(DetailView):
    template_name = "toppings/toppings_detail.html"
    model = Topping
