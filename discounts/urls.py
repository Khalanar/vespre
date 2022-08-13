from django.urls import path
from . import views

urlpatterns = [

    path('', views.discounts, name="discounts"),
    path('add/', views.add_discount, name="add_discount"),
    path('delete/<int:discount_id>/', views.delete_discount, name="delete_discount"),
    path('apply/', views.apply_discount, name="apply_discount"),
]
