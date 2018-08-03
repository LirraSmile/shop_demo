# import from Django add-methods in admin (???)
from django.contrib import admin
# import our model Product
from .models import Product

# tell admin panel 'register our model Product'
admin.site.register(Product)
