# import standard model class from Django
from django.db import models

from django.urls import reverse

# Create a basic model of our product
class Product(models.Model):
    def __str__(self):
        return self.title 
    
    title = models.CharField(max_length=200) # specify maximum length
    description = models.TextField(max_length=5000, blank=True)
    category = models.ForeignKey(
        'Category', 
        on_delete='CASCADE',
        related_name='products', 
        null=True)

    def get_absolute_url(self):
        return reverse('ProductDetail', args=[str(self.id)])

class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, blank=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        id = product.category.id
        return reverse('ProductListByCategory', args=[str(self.id)])

    def __str__(self):
        return self.title