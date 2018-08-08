# import from Django add-methods in admin (???)
from django.contrib import admin
# import our models
from .models import Product
from .models import Category

# tell admin panel 'register our model Product'
admin.site.register(Product)
# tell admin panel 'register our model Category'
admin.site.register(Category)
