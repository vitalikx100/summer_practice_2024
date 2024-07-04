from django.shortcuts import render


def city_home(request):
    return render(request, 'citystreetshop/city.html')