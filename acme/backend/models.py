from django.db import models


class Customer(models.Model):
    id_number = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=200)


class Vet(models.Model):
    id_number = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=14)


class Cashier(models.Model):
    id_number = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class Pet(models.Model):
    id_pet = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=200)
    sex = models.CharField(max_length=200)
    birth_date = models.CharField(max_length=10)
    animal_type = models.CharField(max_length=200)
    owner = models.ManyToManyField(Customer)


class Service(models.Model):
    id_service = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    cost = models.IntegerField()
    state = models.CharField(max_length=200)
    

class Record(models.Model):
    id_record = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    date = models.CharField(max_length=10)
    vet = models.ManyToManyField(Vet)
    service = models.ManyToManyField(Service)
    pet = models.ManyToManyField(Pet)
    state = models.CharField(max_length=20)


class Bill(models.Model):
    id_bill = models.AutoField(primary_key=True)
    record = models.ManyToManyField(Record)
    cost = models.IntegerField()


class Administrator(models.Model):
    user = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=200)
   
