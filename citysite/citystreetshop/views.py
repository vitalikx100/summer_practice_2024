from django.shortcuts import render, redirect
from .forms import ShopForm
from .models import City, Street, Shop
from django.views.generic import DetailView, ListView
from django.utils import timezone
import datetime
from django.db.models import Q, F


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
    is_open = request.GET.get('open')

    current_time = timezone.now().time()

    shops = Shop.objects.all()

    if city_id:
        shops = shops.filter(city_id=city_id)
    if street_id:
        shops = shops.filter(street_id=street_id)

    if is_open is not None:
        is_open = int(is_open)
        if is_open == 1:
            # Магазин открыт
            shops = shops.filter(
                Q(time_open__lt=F('time_close')) & Q(time_open__lte=current_time) & Q(time_close__gte=current_time) |
                Q(time_open__gt=F('time_close')) & (Q(time_open__lte=current_time) | Q(time_close__gte=current_time))
            )
        elif is_open == 0:
            # Магазин закрыт
            shops = shops.exclude(
                Q(time_open__lt=F('time_close')) & Q(time_open__lte=current_time) & Q(time_close__gte=current_time) |
                Q(time_open__gt=F('time_close')) & (Q(time_open__lte=current_time) | Q(time_close__gte=current_time))
            )

    # if is_open is not None:
        #        is_open = int(is_open)
        #       if is_open == 1:
        #            shops = shops.filter(time_open__lte=current_time, time_close__gte=current_time)
        #       elif is_open == 0:
        #           shops = shops.exclude(time_open__lte=current_time, time_close__gte=current_time)

    data = {
        'shops': shops,
    }

    return render(request, 'citystreetshop/shops_view.html', data)
