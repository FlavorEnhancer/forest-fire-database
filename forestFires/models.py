from django.db import models


# create models here
class Bills(models.Model):
    id = models.IntegerField(primary_key=True)
    fc_id = models.ForeignKey()
    fire_id = models.ForeignKey()
    treatment_id = models.IntegerField()
    monetary_value = models.DecimalField(max_digits=8, decimal_places=2)


class Contract(models.Model):
    id = models.IntegerField(primary_key=True)
    fc_id = models.ForeignKey()
    name = models.CharField()
    content = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()


class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    fc_id = models.ForeignKey()
    ssn = models.CharField()
    name = models.CharField()
    dob = models.DateField()
    sex = models.CharField()
    address = models.CharField()
    supervisor_id = models.IntegerField()


class Evac_site(models.Model):
    id = models.IntegerField(primary_key=True)
    fire_id = models.ForeignKey()
    location_id = models.ForeignKey()
    acres = models.IntegerField()


class Fire(models.Model):
    id = models.IntegerField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    acres = models.IntegerField()
    cause = models.CharField()
    kelvin = models.IntegerField()


class Fire_burn_locations(models.Model):
    fire_id = models.ForeignKey()
    location_id = models.ForeignKey()


class Fire_contractor(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.CharField()
    phone = models.CharField()
    name = models.CharField()


class Fire_contractor_fires(models.Model):
    fc_id = models.ForeignKey()
    fire_id = models.ForeignKey()


class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField()
    latitude = models.DecimalField()
    longitude = models.DecimalField()


class Tool(models.Model):
    id = models.IntegerField()
    fc_id = models.ForeignKey()
    description = models.TextField()
    name = models.CharField()


class Treatment(models.Model):
    id = models.IntegerField(primary_key=True)
    fc_id = models.ForeignKey()
    fire_id = models.ForeignKey()
    description = models.TextField()


class Vehicle(models.Model):
    id = models.IntegerField(primary_key=True)
    fc_id = models.ForeignKey()
    type = models.CharField()
    capacity = models.IntegerField()
    fuel = models.CharField()


class Victim(models.Model):
    id = models.IntegerField(primary_key=True)
    fire_id = models.ForeignKey()
    evac_site_id = models.ForeignKey()
    location_id = models.ForeignKey()
    ssn = models.CharField()
    dob = models.DateField()
    sex = models.CharField()
    address = models.CharField()
