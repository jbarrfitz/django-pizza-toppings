from django.urls import path

from .views import ToppingsListView, ToppingsDetailView

urlpatterns = [
    path('all/', ToppingsListView.as_view(), name="toppings_list"),
    path('<int:pk>/', ToppingsDetailView.as_view(), name="toppings_detail")
]