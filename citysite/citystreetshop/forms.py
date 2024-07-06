from .models import City
from .models import Street
from .models import Shop
from django.forms import ModelForm, TextInput, TimeInput, Select

class ShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = ['title', 'city', 'street', 'building', 'time_open', 'time_close']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название магазина'
            }),
            'city': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Город'
            }),
            'street': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Улица'
            }),
            'building': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дом'
            }),
            'time_open': TimeInput(attrs={
                'type': 'time',
                'class': 'form-control',
                'placeholder': 'Время открытия'
            }),
            'time_close': TimeInput(attrs={
                'type': 'time',
                'class': 'form-control',
                'placeholder': 'Время закрытия'
            }),
        }
