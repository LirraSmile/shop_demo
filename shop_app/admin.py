# import from Django add-methods in admin (???)
from django.contrib import admin
# import our model Product
from .models import Product
from .models import Category

# tell admin panel 'register our model Product'
admin.site.register(Product)

admin.site.register(Category)
