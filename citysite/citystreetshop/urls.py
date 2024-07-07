from django.urls import path
from . import views

urlpatterns = [
    path('', views.CityAPIAll.as_view(), name='cities'),
    path('shop/', views.shop_create, name='shop_create'),
    path('shops/', views.shop_view, name='shops_view'),
    path('<int:pk>/street', views.CityStreet.as_view(), name='city-street')
]