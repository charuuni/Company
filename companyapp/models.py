from django.db import models

# Create your models here.
class company(models.Model):
     companyname=models.CharField(max_length=10)
     companyaddress=models.TextField(max_length=100)
     contactnumber=models.CharField(max_length=10)
     companyimage=models.ImageField(upload_to='pic',default='null.jpg')

