from django.shortcuts import render

# import model for CBV            
from django.views import generic 

# import our model Product
from .models import Product

class ProductListView(generic.ListView):    
    template_name = 'products_list.html' # plug-in our template
    # inform under what name data will be transferred to the template
    context_object_name = 'products' 
    model = Product # name of model

class ProductDetail(generic.DetailView): 
    template_name = 'product_detail.html' 
    model = Product

# method for adding additional information to the context
def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    # pass a list of all categories to the context dictionary
    context['categories'] = Category.objects.all()
    return context


