from django.shortcuts import render


def city_home(request):
    return render(request, 'citystreetshop/city.html')


def shop_create(request):
    return render(request, 'citystreetshop/shop_create.html')