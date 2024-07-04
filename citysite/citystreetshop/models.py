from django.db import models

class City(models.Model):
    title = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = "Города"

class Street(models.Model):
    title = models.CharField('Название', max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Улицу'
        verbose_name_plural = "Улицы"

class Shop(models.Model):
    title = models.CharField('Название', max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    building = models.CharField('Дом', max_length=100)
    time_open = models.TimeField('Время открытия')
    time_close = models.TimeField('Время закрытия')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = "Магазины"

