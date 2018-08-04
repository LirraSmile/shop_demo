"""django_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# import our file views of shop_app
from shop_app import views 

# we are talking Django about what we want to display our view on the main page
# and the line belowthe link to our admin
urlpatterns = [
    path('', views.ProductListView.as_view(), name='index'),
    path('category/<int:pk>/', views.CategoryDetail.as_view(), name='detail'),
    path('product/<int:pk>/', views.ProductDetail.as_view(), name='detail'),
    path('admin/', admin.site.urls),
]
