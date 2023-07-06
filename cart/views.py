from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product
from .models import CartItem, Order

def order_confirmation(request):
    return render(request, 'cart/order_confirmation.html')


def place_order(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        payment_method = request.POST['payment_method']

        print(f"Name: {name}")
        print(f"Phone Number: {phone_number}")
        print(f"Address: {address}")
        print(f"Payment Method: {payment_method}")

        order = Order.objects.create(name=name, phone_number=phone_number, address=address,
                                     payment_method=payment_method)
        # You can also associate cart items with the order if needed
        cart_items = CartItem.objects.all()
        for cart_item in cart_items:
            cart_item.order = order
            cart_item.save()
        # Clear the cart after placing the order
        CartItem.objects.all().delete()
        return render(request, 'cart/order_confirmation.html', {'order': order})
    else:
        return render(request, 'cart/place_order.html')


def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        product = get_object_or_404(Product, id=product_id)
        cart_item, created = CartItem.objects.get_or_create(product=product, defaults={'quantity': 1})
        if not created:
            cart_item.quantity += 1
            cart_item.save()
    return redirect(request.META.get('HTTP_REFERER'))


def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart:cart_view')


def update_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('cart:cart_view')


def cart_view(request):
    cart_items = CartItem.objects.all()
    total = sum(item.subtotal() for item in cart_items)
    return render(request, 'cart/cart_view.html', {'cart_items': cart_items, 'total': total})
