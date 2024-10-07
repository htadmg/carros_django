from django.shortcuts import render
from cars.models import Car


def cars_views(request):
    cars = Car.objects.filter(brand=4)

    return render(
        request,
        'cars.html',
        {'cars' : cars }
    )