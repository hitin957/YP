# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.core.validators import MinLengthValidator
from django.db import models


class BuildMaterials(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название строительного материала', null=False)
    description = models.CharField(max_length=225, blank=True, null=True, verbose_name='Описание сторительного материала',)
    price = models.IntegerField(verbose_name='Цена строительного материала', null=False)
    fk_speshal_car = models.ForeignKey('SpeshalCar', models.DO_NOTHING, db_column='fk_speshal_car', verbose_name='Специальная техника', null=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'build_materials'


class Costumer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', null=False)
    surname = models.CharField(max_length=100, verbose_name='Фамилия', null=False)
    middlename = models.CharField(max_length=100, verbose_name='Отчество', null=False)
    numberphone = models.CharField(unique=True, max_length=11, verbose_name='номер телефона', null=False)
    useremail = models.CharField(unique=True, max_length=25, verbose_name='адрес электорной почты', null=False)
    birthday = models.DateField(verbose_name='дата рождения',null=False)
    address_of_the_building = models.CharField(unique=True, max_length=30, verbose_name='Адресс территории строительства', null=False)
    fk_employee = models.ForeignKey('Employee', models.DO_NOTHING, db_column='fk_employee', verbose_name='Сотрудник', null=False)
    fk_materials = models.ForeignKey(BuildMaterials, models.DO_NOTHING, db_column='fk_materials', verbose_name='Материал', null=False)
    fk_service = models.ForeignKey('Service', models.DO_NOTHING, db_column='fk_service', verbose_name='Услуга', null=False)

    def __str__(self):
        return f'{self.name} {self.surname} {self.middlename}'

    class Meta:
        db_table = 'costumer'


class Employee(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', null=False)
    surname = models.CharField(max_length=100, verbose_name='Фамилия', null=False)
    middlename = models.CharField(max_length=100, blank=True, null=True, verbose_name='Отчество')
    numberphone = models.CharField(unique=True, max_length=11, verbose_name='номер телефона', null=False)
    useremail = models.CharField(unique=False, max_length=25, verbose_name='Электроная почта', null=False)
    birthday = models.DateField(verbose_name='дата рождения', null=False)
    password = models.CharField(max_length=15, verbose_name='пароль', null=False)
    post = models.CharField(max_length=225, verbose_name='Должность', null=False)

    def __str__(self):
        return f'{self.name} {self.surname} {self.middlename}'

    class Meta:
        db_table = 'employee'


class Service(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(10)], verbose_name='Название услуги', null=False)
    description = models.CharField(max_length=225, blank=True, null=True, verbose_name='Описание услуги')
    price = models.IntegerField(verbose_name='Цена услуги', null=False)
    fk_speshal_car = models.ForeignKey('SpeshalCar', models.DO_NOTHING, db_column='fk_speshal_car', verbose_name='Специальная техника', null=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'service'


class SpeshalCar(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название техники', null=False)
    description = models.CharField(max_length=225, blank=True, null=True, verbose_name='Описание техники')

    GYSENIZA = 'Гусенечная'
    KOLESNIE = 'Колёсная'

    TYPE_CAR = [
        (GYSENIZA, 'Гусенечная'),
        (KOLESNIE, 'Колёсная')
    ]

    type_car = models.CharField(max_length=15, choices=TYPE_CAR, verbose_name='Тип техники', null=False)
    fk_employee = models.ForeignKey(Employee, models.DO_NOTHING, db_column='fk_employee', verbose_name='Водитель', null=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'speshal_car'
