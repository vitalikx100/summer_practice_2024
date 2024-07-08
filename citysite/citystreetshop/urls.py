from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('city/', views.CityAPIAll.as_view(), name='cities'),
    path('shop/', views.ShopCreateAPIView.as_view(), name='shop_create'),
    path('shops/', views.shop_view, name='shops_view'),
    path('city/<int:pk>/street', views.CityStreetAPIAll.as_view(), name='city-street')
]