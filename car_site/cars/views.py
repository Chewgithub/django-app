from django.shortcuts import render, redirect
from django.urls import reverse
from . import models


# Create your views here.
def list(request):
    all_cars=models.Car.objects.all()
    context={"cars":all_cars}
    return render(request,'cars/list.html', context=context)

def delete(request):
    if request.POST:
        pk=request.POST['pk']
        try:
            models.Car.objects.get(pk=pk).delete()
            
            #if user delete a car, go to list
            # car:list (car omes from app_name, list come from name=list)
            return redirect(reverse('cars:list'))
        except:
            print("pk not found")
            return redirect(reverse('cars:list'))
    else:
        return render(request,'cars/delete.html')


def add(request):
    if request.POST:
        brand=request.POST['brand']
        year=int(request.POST['year'])
        models.Car.objects.create(brand=brand,year=year)

        #if user submit a new car, go to list
        # car:list (car omes from app_name, list come from name=list)
        return redirect(reverse('cars:list'))
    else:
        return render(request,'cars/add.html')