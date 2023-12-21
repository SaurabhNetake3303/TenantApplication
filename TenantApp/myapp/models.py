from django.db import models

# Create your models here.

class employee(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=50,default="0")
    password = models.CharField(max_length=20,default="0")

class Tenantname(models.Model):
    FlatNumber = models.CharField(max_length=100,default="0")
    name = models.CharField(max_length=20,default="0")
    Address = models.CharField(max_length=255,default="0")
    Adhar = models.CharField(max_length=50,default="0")
    todaysdate = models.CharField(max_length=20,default="0")
    rent = models.CharField(max_length=20,default="0")
    phone = models.CharField(max_length=50,default="0")

    class Meta:
         db_table="myapp_tenantname"

class Mainmeter(models.Model):
     meterNo = models.CharField(max_length=100,default="0")
     month = models.CharField(max_length=20,default="0")
     year = models.CharField(max_length=50,default="0")
     todaysdate = models.CharField(max_length=20,default="0")
     unitConsumed = models.CharField(max_length=50,default="0")
     amount = models.CharField(max_length=20,default="0")

     class Meta:
         db_table="myapp_mainmeter"

class Submeter(models.Model):
     tenantName = models.CharField(max_length=100,default="0")
     meterID = models.CharField(max_length=20,default="0")
     todaysdate = models.CharField(max_length=20,default="0")
     previousReading = models.CharField(max_length=50,default="0")
     currentReading = models.CharField(max_length=50,default="0")
     amount = models.CharField(max_length=20,default="0")

     class Meta:
         db_table="myapp_Submeter"

class Tankerentry(models.Model):
     month = models.CharField(max_length=20)
     year = models.CharField(max_length=50)
     todaysdate = models.CharField(max_length=20,default="0")
     totalTanker = models.CharField(max_length=100)
     amtPerTanker = models.CharField(max_length=50)
     numOfTenants = models.CharField(max_length=20)

     class Meta:
         db_table="myapp_Tankerentry"

