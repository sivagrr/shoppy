from django.shortcuts import redirect, render
from .models import Product
from .forms import ProductForm

def home_page(request):
    return render(request, 'shoppy.html')


def about_page(request):
    return render(request, 'about.html')


def products_page(request):
    products = Product.objects.all().order_by('name')
    return render(request, 'products.html', {'products': products})

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")
    else:
        form = ProductForm()

    return render(request, "addproduct.html", {"form": form})