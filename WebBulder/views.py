import xlwt as xlwt
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from .models import *
from .forms import *
# Create your views here.


def main(request):
    Servic = Service.objects.all()
    return render(request, 'Main.html', {'Servic': Servic})


def main_filter(request, price_min, price_max):
    Servic = Service.objects.all()
    if price_max>price_min:
        Servic = Servic.order_by('price')
    elif price_min>price_max:
        Servic = Servic.order_by('-price')
    return render(request, 'Main.html', {'Servic': Servic})


def Manager(request):
    return render(request, 'Manager.html')


#Заказы(1)
def CostumersSel(request):
    CostumerSel = Costumer.objects.all()
    return render(request, 'Costumers/Costumers_select.html', {'CostumerSel': CostumerSel})


#Услуги(2)
def ServiceSel(request):
    ServiceSel = Service.objects.all()
    return render(request, 'Service/Service_select.html', {'ServiceSel': ServiceSel})


def ServiceSel_filter(request, price_min, price_max):
    ServiceSel = Service.objects.all()
    if price_max>price_min:
        ServiceSel = ServiceSel.order_by('price')
    elif price_min>price_max:
        ServiceSel = ServiceSel.order_by('-price')
    return render(request, 'Service/Service_select.html', {'ServiceSel': ServiceSel})


#Материалы(3)
def Build_MaterialsSel(request):
    Build_MaterialsSel = BuildMaterials.objects.all()
    return render(request, 'Builder_Materials/Builder_Materials_select.html', {'Build_MaterialsSel': Build_MaterialsSel})


#Специальная техника(4)
def Speshal_CarSel(request):
    Speshal_CarSel = SpeshalCar.objects.all()
    return render(request, 'Speshal_Car/Speshal_Car_select.html', {'Speshal_CarSel': Speshal_CarSel})


def Speshal_CarSel_filter(request, type_car):
    Speshal_CarSel = SpeshalCar.objects.filter(type_car=type_car)
    return render(request, 'Speshal_Car/Speshal_Car_select.html', {'Speshal_CarSel': Speshal_CarSel})


#Сотрудники(5)
def EmployessSel(request):
    EmployessSel = Employee.objects.all()
    return render(request, 'Employes/Employes_select.html', {'EmployessSel': EmployessSel})


def EmployessSel_filter(request, price_min, price_max):
    EmployessSel = Employee.objects.all()
    if price_max>price_min:
        EmployessSel = EmployessSel.order_by('surname')
    elif price_min>price_max:
        EmployessSel = EmployessSel.order_by('-surname')
    return render(request, 'Employes/Employes_select.html', {'EmployessSel': EmployessSel})


##Заказы(1)


class CostumersAdd(CreateView):
    model = Costumer
    template_name = 'Costumers/Costumers_add.html'
    form_class = CostumerForm
    success_url = reverse_lazy('Main')

    def get_success_url(self):
        messages.success(self.request, 'Заказ успешно добавлен')
        return super().get_success_url()


class CostumersUpdate(UpdateView):
    model = Costumer
    form_class = CostumerForm
    template_name = 'Costumers/Costumers_update.html'
    success_url = reverse_lazy('Main')

    def get_success_url(self):
        messages.success(self.request, 'Заказ успешно изменён')
        return super().get_success_url()


class CostumersDelete(DeleteView):
    model = Costumer
    template_name = 'Costumers/Costumers_delet.html'
    success_url = reverse_lazy('Main')

    def get_success_url(self):
        messages.success(self.request, 'Заказ успешно удалён')
        return super().get_success_url()


##Услуги(2)


class ServiceAdd(CreateView):
    model = Service
    template_name = 'Service/Service_add.html'
    form_class = ServiceForms
    success_url = reverse_lazy('ServiceSel')

    def get_success_url(self):
        messages.success(self.request, 'Услуга успешна добавлена')
        return super().get_success_url()


class ServiceUpdate(UpdateView):
    model = Service
    form_class = ServiceForms
    template_name = 'Service/Service_update.html'
    success_url = reverse_lazy('ServiceSel')

    def get_success_url(self):
        messages.success(self.request, 'Услуга успешна изменена')
        return super().get_success_url()


class ServiceDelete(DeleteView):
    model = Service
    template_name = 'Service/Service_delet.html'
    success_url = reverse_lazy('ServiceSel')

    def get_success_url(self):
        messages.success(self.request, 'Услуга успешна удалена')
        return super().get_success_url()


##Специальная техника(3)


class SpeshalCarAdd(CreateView):
    model = SpeshalCar
    template_name = 'Speshal_Car/Speshal_Car_add.html'
    form_class = Speshal_CarForms
    success_url = reverse_lazy('Speshal_CarSel')

    def get_success_url(self):
        messages.success(self.request, 'Специальная техника успешна добавлена')
        return super().get_success_url()


class SpeshalCarUpdate(UpdateView):
    model = SpeshalCar
    form_class = Speshal_CarForms
    template_name = 'Speshal_Car/Speshal_Car_update.html'
    success_url = reverse_lazy('Speshal_CarSel')

    def get_success_url(self):
        messages.success(self.request, 'Специальная техника успешна изменена')
        return super().get_success_url()


class SpeshalCarDelete(DeleteView):
    model = SpeshalCar
    template_name = 'Speshal_Car/Speshal_Car_delet.html'
    success_url = reverse_lazy('Speshal_CarSel')

    def get_success_url(self):
        messages.success(self.request, 'Специальная техника успешна удалена')
        return super().get_success_url()


##Материалы(4)


class MaterialsAdd(CreateView):
    model = BuildMaterials
    template_name = 'Builder_Materials/Builder_Materials_add.html'
    form_class = MaterialsForms
    success_url = reverse_lazy('Build_MaterialsSel')

    def get_success_url(self):
        messages.success(self.request, 'Строительный материал успешно добавлен')
        return super().get_success_url()


class MaterialsUpdate(UpdateView):
    model = BuildMaterials
    form_class = MaterialsForms
    template_name = 'Builder_Materials/Builder_Materials_update.html'
    success_url = reverse_lazy('Build_MaterialsSel')

    def get_success_url(self):
        messages.success(self.request, 'Строительный материал успешно изменён')
        return super().get_success_url()


class MaterialsDelete(DeleteView):
    model = BuildMaterials
    template_name = 'Builder_Materials/Builder_Materials_delet.html'
    success_url = reverse_lazy('Build_MaterialsSel')

    def get_success_url(self):
        messages.success(self.request, 'Строительный материал успешно удалён')
        return super().get_success_url()


##Сотрудники(5)


class EmployesAdd(CreateView):
    model = Employee
    template_name = 'Employes/Employes_add.html'
    form_class = EmployesForms
    success_url = reverse_lazy('EmployessSel')

    def get_success_url(self):
        messages.success(self.request, 'Сотрудник успешно добавлен')
        return super().get_success_url()


class EmployesUpdate(UpdateView):
    model = Employee
    form_class = EmployesForms
    template_name = 'Employes/Employes_update.html'
    success_url = reverse_lazy('EmployessSel')

    def get_success_url(self):
        messages.success(self.request, 'Сотрудник успешно изменён')
        return super().get_success_url()


class EmployesDelete(DeleteView):
    model = Employee
    template_name = 'Employes/Employes_delet.html'
    success_url = reverse_lazy('EmployessSel')

    def get_success_url(self):
        messages.success(self.request, 'Сотрудник успешно удалён')
        return super().get_success_url()


def athu(request):
    input_pass = request.POST.get('input_pass')
    input_emaill = request.POST.get('input_emaill')
    print(input_pass)
    print(input_emaill)
    Employeeall = Employee.objects.all()
    for i in Employeeall:
        if i.password == input_pass and i.useremail == input_emaill and (i.post == 'Менеджер' or i.post == 'менеджер'):
            return render(request, 'Manager.html')
        elif i.password == input_pass and i.useremail == input_emaill:
            Employeeall = Employee.objects.filter(useremail=i.useremail)
            return render(request, 'Employess.html', {'Employeeall': Employeeall})
    return render(request, 'Auth.html')


def athu_users(request):
    input_emaill = request.POST.get('input_emaill')
    print(input_emaill)
    Costumerall = Costumer.objects.all()
    for i in Costumerall:
        if i.useremail == input_emaill:
            Costumerall = Costumer.objects.filter(useremail=input_emaill)
            return render(request, 'Costumers/Costumers_select.html', {'CostumerSel': Costumerall})
    return render(request, 'check.html')


def export_Employes_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Employes.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Employes')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Имя', 'Фамилия', 'Отчество', 'Номер телефона', 'Электроная почта', 'Дата рождения', 'Пароль', 'Должность']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = Employee.objects.all().values_list('name', 'surname', 'middlename', 'numberphone', 'useremail', 'birthday', 'password', 'post')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def export_Speshal_car_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Speshal_car.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Speshal_car')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Название', 'Описание', 'Тип', 'Водитель']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = SpeshalCar.objects.all().values_list('name', 'description', 'type_car', 'fk_employee__surname')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def export_Service_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Service.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Service')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Название', 'Описание', 'Цена', 'Техника']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = Service.objects.all().values_list('name', 'description', 'price', 'fk_speshal_car__name')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def export_Build_Materials_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Build_Materials.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Build_Materials')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Название', 'Описание', 'Цена', 'Доставка']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = BuildMaterials.objects.all().values_list('name', 'description', 'price', 'fk_speshal_car__name')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response