"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from home.views import about_page, add_product, home_page, products_page, delete_product, product_detail, update_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='root'),
    path('h/home', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('products/', products_page, name='products'),
    path("products/add/", add_product, name="addproduct"),
    path("products/<int:product_id>/delete/", delete_product, name="deleteproduct"),
    path("products/detail/<int:product_id>/", product_detail, name="productdetail"),
    path("products/update/<int:product_id>/", update_product, name="updateproduct")
]
