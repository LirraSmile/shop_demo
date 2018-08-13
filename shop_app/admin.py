# import from Django add-methods in admin (???)
from django.contrib import admin
# import our models
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
# tell admin panel 'register our model Product'
admin.site.register(Product, ProductAdmin)
# tell admin panel 'register our model Category'
admin.site.register(Category)
