from django.db import models
from django.contrib.auth.models import User
# Create your models here.







class todo(models.Model):
    checklist= models.CharField(max_length= 1000)
    sprint= models.DateField(blank= True ,null= True)
    user = models.ForeignKey (User,on_delete=models.CASCADE)

    def __str__(self) :
        return f'{ self.user })'


