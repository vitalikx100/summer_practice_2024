from django.shortcuts import render, redirect
from .forms import ShopForm
from .models import City, Street, Shop
from django.views.generic import DetailView
from django.utils import timezone
from django.db.models import Q, F
from rest_framework import generics
from .serializers import CitySerializer


class CityAPIAll(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityStreet(DetailView):
    model = City
    template_name = 'citystreetshop/street.html'
    context_object_name = 'city'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city = self.object
        context['streets'] = Street.objects.filter(city=city)
        return context


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

    current_time = timezone.localtime(timezone.now())

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

    data = {
        'shops': shops,
        'current_time': current_time
    }

    return render(request, 'citystreetshop/shops_view.html', data)
