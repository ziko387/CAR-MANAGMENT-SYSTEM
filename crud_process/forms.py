from django import forms
from .models import CarItems

class CarForms(forms.ModelForm):
    class Meta:
        model = CarItems
        fields = ['car_name', 'car_model', 'car_image', 'car_price']
        
        