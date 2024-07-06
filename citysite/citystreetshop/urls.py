from django.urls import path
from . import views

urlpatterns = [
    path('', views.city_all, name='cities'),
    path('shop/', views.shop_create, name='shop_create'),
    path('<int:pk>/street', views.CityStreet.as_view(), name='city-street')
]