from .forms import ProductForm
from .models import Category
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import AddToCartForm

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            # Add the product to the cart or update the quantity
            cart = request.session.get('cart', {})
            cart[str(product.pk)] = quantity
            request.session['cart'] = cart
            return redirect('cart:cart_detail')
    else:
        form = AddToCartForm()
    return render(request, 'products/product_detail.html', {'product': product, 'form': form})


def product_list(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            quantity = form.cleaned_data['quantity']
            # Add the product to the cart or update the quantity
            cart = request.session.get('cart', {})
            cart[str(product_id)] = quantity
            request.session['cart'] = cart
            return redirect('cart:cart_detail')
    else:
        form = AddToCartForm()
    return render(request, 'products/product_list.html', {'products': products, 'form': form})

# def product_create(request):
#     if request.method == 'POST':
#         # Process the form submission and create a new product
#         name = request.POST['name']
#         price = request.POST['price']
#         category_id = request.POST['category']
#         image = request.FILES['image']
#         category = get_object_or_404(Category, pk=category_id)
#         product = Product(name=name, price=price, category=category, image=image)
#         product.save()
#         return redirect('products:product_list')
#     else:
#         # Render the product creation form
#         categories = Category.objects.all()
#         return render(request, 'products/product_create.html', {'categories': categories})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            # Redirect to the product detail page or product list
            return redirect('products:product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'products/product_create.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        # Process the form submission and update the product
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.category_id = request.POST['category']
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.save()
        return redirect('products:product_list')
    else:
        # Render the product update form
        categories = Category.objects.all()
        return render(request, 'products/product_update.html', {'product': product, 'categories': categories})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('products:product_list')

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            # Redirect to the product detail page or product list
            return redirect('products:product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'products/product_create.html', {'form': form})
