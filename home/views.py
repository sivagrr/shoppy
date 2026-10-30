from django.shortcuts import get_object_or_404, redirect, render
from .models import Product
from .forms import ProductForm

def home_page(request):
    return render(request, 'shoppy.html')


def about_page(request):
    return render(request, 'about.html')


def products_page(request):
    products = Product.objects.all().order_by('name')
    return render(request, 'products.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")
    else:
        form = ProductForm()

    return render(request, "addproduct.html", {"form": form})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.delete()
        return redirect("products")
    return render(request, "deleteproduct.html", {"product": product})

def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("products")
    else:
        form = ProductForm(instance=product)

    return render(request, "updateproduct.html", {"form": form, "product": product})
