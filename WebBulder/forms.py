from django import forms
from .models import *


class CostumerForm(forms.ModelForm):#заказы для пользователя(1.1)
    class Meta:
        model = Costumer
        fields = '__all__'


class ServiceForms(forms.ModelForm):#услуги(2)
    class Meta:
        model = Service
        fields = '__all__'


class MaterialsForms(forms.ModelForm):#материалы(3)
    class Meta:
        model = BuildMaterials
        fields = '__all__'


class Speshal_CarForms(forms.ModelForm):#специальная техника(4)
    class Meta:
        model = SpeshalCar
        fields = '__all__'


class EmployesForms(forms.ModelForm):#сотрудники(5)
    class Meta:
        model = Employee
        fields = '__all__'