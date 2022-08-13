from django.urls import path
from . import views

urlpatterns = [
    path('wishlist/<int:item_id>/', views.add_to_wishlist, name='add_to_wishlist'),
]