from django.shortcuts import render
from cars.models import Car
from cars.forms import CarForm

def cars_views(request):
    cars = Car.objects.all()
    search = request.GET.get('search')
    
    if search:
        cars = cars = cars.filter(model__contains=search)

    return render(
        request,
        'cars.html',
        {'cars' : cars }
    )


def new_car_views(request):
    if request.method == "POST": 
        pass
    else:
        new_car_form = CarForm()

    return render(request, 'new_car.html', {'new_car_form': new_car_form })
