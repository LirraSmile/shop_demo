from django.shortcuts import render

# import model for CBV            
from django.views import generic 

# import our model Product
from .models import Product

class ProductListView(generic.ListView):
    
    template_name = 'products_list.html' # plug-in our template
    context_object_name = 'products' # inform under what name data will be transferred to the template
    model = Product # name of model

# The standard view is a regular Python function that gets the request 
"""def index(request):
    request_method = request.method
    
    ip_address = request.META['REMOTE_ADDR']
    browser_info = request.META['HTTP_USER_AGENT']
    
    response_text = "Тип запроса: {}. IP-адрес: {}. ЮзерАгент: {}".format(request_method, ip_address, browser_info)
    
    return HttpResponse(response_text)"""


