"""
URL configuration for YP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from WebBulder import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='Main'),
    path('<int:price_min>/<int:price_max>', views.main_filter, name='Main'),
    path('Manager/', views.Manager, name='Manager'),
    path('Auth/', views.athu, name='auth'),

    path('ServiceSel/', views.ServiceSel, name='ServiceSel'),
    path('ServiceSel/<int:price_min>/<int:price_max>', views.ServiceSel_filter, name='ServiceSel'),

    path('Speshal_CarSel/', views.Speshal_CarSel, name='Speshal_CarSel'),
    path('Speshal_CarSel/<str:type_car>', views.Speshal_CarSel_filter, name='Speshal_CarSel'),

    path('Build_MaterialsSel/', views.Build_MaterialsSel, name='Build_MaterialsSel'),

    path('EmployessSel/', views.EmployessSel, name='EmployessSel'),
    path('EmployessSel/<int:price_min>/<int:price_max>', views.EmployessSel_filter, name='EmployessSel'),

    path('check/', views.athu_users, name='check'),

    #Заказы(1)
    path('CostumersSel/', views.CostumersSel, name='CostumersSel'),

    path('CostumersAdd/', views.CostumersAdd.as_view(), name='CostumersAdd'),
    path('CostumersUpd/<int:pk>', views.CostumersUpdate.as_view(), name='CostumersUpd'),
    path('CostumersDel/<int:pk>', views.CostumersDelete.as_view(), name='CostumersDel'),

    #Услуги(2)
    path('ServiceAdd/', views.ServiceAdd.as_view(), name='ServiceAdd'),
    path('ServiceUpdate/<int:pk>', views.ServiceUpdate.as_view(), name='ServiceUpdate'),
    path('ServiceDelete/<int:pk>', views.ServiceDelete.as_view(), name='ServiceDelete'),

    path('export_Service_xls/', views.export_Service_xls, name='export_Service_xls'),

    #Специальная техника(3)
    path('SpeshalCarAdd/', views.SpeshalCarAdd.as_view(), name='SpeshalCarAdd'),
    path('SpeshalCarUpdate/<int:pk>', views.SpeshalCarUpdate.as_view(), name='SpeshalCarUpdate'),
    path('SpeshalCarDelete/<int:pk>', views.SpeshalCarDelete.as_view(), name='SpeshalCarDelete'),

    path('export_Speshal_car_xls/', views.export_Speshal_car_xls, name='export_Speshal_car_xls'),

    #Материалы(4)
    path('MaterialsAdd', views.MaterialsAdd.as_view(), name='MaterialsAdd'),
    path('MaterialsUpdate/<int:pk>', views.MaterialsUpdate.as_view(), name='MaterialsUpdate'),
    path('MaterialsDelete/<int:pk>', views.MaterialsDelete.as_view(), name='MaterialsDelete'),

    path('export_Build_Materials_xls/', views.export_Build_Materials_xls, name='export_Build_Materials_xls'),

    #Сотрудники(5)
    path('EmployesAdd', views.EmployesAdd.as_view(), name='EmployesAdd'),
    path('EmployesUpdate/<int:pk>', views.EmployesUpdate.as_view(), name='EmployesUpdate'),
    path('EmployesDelete/<int:pk>', views.EmployesDelete.as_view(), name='EmployesDelete'),

    path('export_Employes_xls/', views.export_Employes_xls, name='export_Employes_xls')

]