# import standard model class from Django
from django.db import models

# Create a basic model of our product
class Product(models.Model):
    def __str__(self):
        return self.title 
    
    title = models.CharField(max_length=200) # specify maximum length
    description = models.TextField(max_length=5000)