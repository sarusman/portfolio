from django.db import models

class Formation(models.Model):
	ids=models.CharField(max_length=2000)
	titre=models.CharField(max_length=2000)
	lieu=models.CharField(max_length=2000)
	datee=models.CharField(max_length=2000)
	address=models.CharField(max_length=2000)
	image=models.CharField(max_length=5000)

class Projets(models.Model):
	ids=models.CharField(max_length=2000)
	titre=models.CharField(max_length=2000)
	datee=models.CharField(max_length=2000)
	desciption=models.CharField(max_length=5000)
	image=models.CharField(max_length=5000)
	langage=models.CharField(max_length=5000)