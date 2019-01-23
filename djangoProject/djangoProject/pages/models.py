from django.db import models

class person(models.Model):
	first_name= models.CharField(max_length=50)
	last_name= models.CharField(max_length=50)
	mobile_number= models.CharField(max_length=10)

class detail(models.Model):
	people=models.ForeignKey(person, on_delete=models.CASCADE)
	p1=models.CharField(max_length=20)
