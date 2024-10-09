from django.shortcuts import render, redirect
from cars.models import Car
from .forms import CarModelForm

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
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarModelForm()

    return render(request, 'new_car.html', {'new_car_form': new_car_form })
