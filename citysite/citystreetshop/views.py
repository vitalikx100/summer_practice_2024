from django.shortcuts import render, redirect
from .forms import ShopForm
from .models import City, Street, Shop
from django.views.generic import DetailView, ListView

class CityStreet(DetailView):
    model = Street
    template_name = 'citystreetshop/street.html'
    context_object_name = 'street'

def city_all(request):
    cities = City.objects.all()
    return render(request, 'citystreetshop/city.html', {'cities': cities})


def shop_create(request):
    error = ''
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Ошибка создания формы'

    form = ShopForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'citystreetshop/shop_create.html', data)

def shop_view(request):
    street_id = request.GET.get('street')
    city_id = request.GET.get('city')

    shops = Shop.objects.all()
    if city_id:
        shops = shops.filter(city_id=city_id)
    if street_id:
        shops = shops.filter(street_id=street_id)

    data = {
        'shops': shops
    }

    return render(request, 'citystreetshop/shops_view.html', data)
