from django.db import models


# Create your models here.
class Admin1(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = "admin1_table"

    def __str__(self):
        return self.username


class Voter(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    voter_id = models.BigIntegerField(blank=False, unique=True)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    father_name = models.CharField(max_length=100, blank=False)
    mother_name = models.CharField(max_length=100, blank=False)
    aadhar = models.CharField(max_length=15, blank=False, unique=True)
    year = models.DateField(blank=False)
    gender_choices = (("MALE", "M"), ("FEMALE", "F"))
    gender = models.CharField(max_length=10, blank=False, choices=gender_choices)
    Street = models.CharField(max_length=100, blank=False)
    contact = models.CharField(max_length=20, blank=False)
    alter_contacts = models.CharField(max_length=20, blank=False)
    zip = models.CharField(max_length=20, blank=False)
    city = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=20, blank=False)
    email = models.CharField(max_length=50, blank=False, unique=True)
    password = models.CharField(max_length=50, blank=False)

    class Meta:
        db_table = "voter_table"

    def __str__(self):
        return self.first_name + " " + self.last_name


class Employee(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    emp_id = models.BigIntegerField(blank=False, unique=True)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    father_name = models.CharField(max_length=100, blank=False)
    mother_name = models.CharField(max_length=100, blank=False)
    aadhar = models.CharField(max_length=15, blank=False, unique=True)
    year = models.DateField(blank=False)
    gender_choices = (("MALE", "M"), ("FEMALE", "F"))
    gender = models.CharField(max_length=10, blank=False, choices=gender_choices)
    Street = models.CharField(max_length=100, blank=False)
    contact = models.CharField(max_length=20, blank=False)
    alter_contacts = models.CharField(max_length=20, blank=False)
    zip = models.CharField(max_length=20, blank=False)
    city = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=20, blank=False)
    email = models.CharField(max_length=50, blank=False, unique=True)
    password = models.CharField(max_length=50, blank=False)

    class Meta:
        db_table = "employee_table"

    def __str__(self):
        return self.first_name + " " + self.last_name


class Contender(models.Model):
    objects = None
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    party = models.CharField(max_length=50, blank=False)
    place = models.CharField(max_length=100, blank=False)
    symb = models.ImageField(blank=False)
    year = models.DateField(blank=False)
    zip = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=20, blank=False)

    class Meta:
        db_table = "contender_table"

    def __str__(self):
        return self.first_name + " " + self.last_name


class votervotemapping(models.Model):
    objects = None
    email = models.CharField(max_length=50, blank=False)

    class Meta:
        db_table = "votervote_table"

    def __str__(self):
        return self.email


class Count(models.Model):
    name = models.CharField(max_length=10,blank=False)
    count = models.IntegerField(blank=False)

    class Meta:
        db_table = "count_table"

    def __str__(self):
        return self.name
