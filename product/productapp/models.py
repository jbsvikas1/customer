from django.db import models

# Create your models here.
class customer_details(models.Model):
 
   
    name = models.CharField(max_length = 100)
    location = models.TextField()
    email = models.EmailField(max_length = 40)
    phonenumber = models.CharField(max_length = 10)
    status = models.CharField(max_length = 20)

    def __str__(self):
        return self.name
