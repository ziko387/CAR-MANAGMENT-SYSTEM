from django.shortcuts import render,redirect,get_object_or_404

from .forms import CarForms
from .models import CarItems

# Create your views here.
def home(request):
    return render(request, 'Html/home.html')

def add_car(request):
    if request.method=='POST':
        form=CarForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form=CarForms()
    return render(request, 'Html/addCar.html',{'form':form})
    
   
       

def car_list(request):
    cars=CarItems.objects.all()
    return render(request, 'Html/carList.html',{'cars':cars})
def update_car(request,pk):
    car = get_object_or_404(CarItems, pk=pk)
    if request.method=='POST':
        form=CarForms(request.POST,request.FILES,instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form=CarForms(instance=car)
    return render(request, 'Html/addCar.html',{'form':form})
def delete_car(request,pk):
    car = get_object_or_404(CarItems, pk=pk)
    if request.method=='POST':
        car.delete()
        return redirect('car_list')
    return render(request, 'Html/confirm.html',{'car':car})
   