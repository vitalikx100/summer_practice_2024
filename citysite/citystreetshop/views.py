from django.shortcuts import render, redirect
from .forms import ShopForm


def city_home(request):
    return render(request, 'citystreetshop/city.html')


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