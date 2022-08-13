from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about-us/', views.about_us, name="about_us"),
    path('policies/<str:template>/', views.policy_pages, name="policy_pages"),
]
