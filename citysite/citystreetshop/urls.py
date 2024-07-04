from django.urls import path
from . import views

urlpatterns = [
    path('', views.city_home, name='home'),
    path('shop/', views.shop_create, name='shop_create')

]