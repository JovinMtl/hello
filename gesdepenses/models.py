from django.db import models

# Create your models here.

class treso(models.Model):
	amount = models.IntegerField()


class Produit(models.Model):
	owner = models.CharField(max_length=40, null=True)
	amount = models.IntegerField()
	desc = models.CharField(max_length = 100, null = True)


class Charge(models.Model):
	owner = models.CharField(max_length=40, null=True)
	amount = models.IntegerField()
	desc = models.CharField(max_length = 100, null = True)


class Main:
	owner : str
	amount : int
	depe : list  #for depenses, charges
	prod : list


	
