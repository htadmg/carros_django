from django.shortcuts import render, redirect
from cars.models import Car
from .forms import CarModelForm
from django.views import View


class CarsView(View):

    def get(self, request):
        cars = Car.objects.all()
        search = request.GET.get('search')
        
        if search:
            cars = cars = cars.filter(model__contains=search)

        return render(
            request,
            'cars.html',
            {'cars' : cars }
        )


class NewCarView(View):
    def get(self, request):
       new_car_form = CarModelForm()
       return render(request, 'new_car.html', {'new_car_form': new_car_form })
    
    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        
        return render(request, 'new_car.html', {'new_car_form': new_car_form })
