from django.urls import path
from . import views

urlpatterns = [
    path('wishlist/<int:item_id>/', views.toggle_from_wishlist, name='toggle_from_wishlist'),
]