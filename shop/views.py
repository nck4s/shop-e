from django.shortcuts import render, redirect
from .models import Product, Order, Customer
from django.db import IntegrityError

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def place_order(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')

        if customer_name and customer_email:
            customer, created = Customer.objects.get_or_create(
                name=customer_name,
                email=customer_email
            )

            order = Order.objects.create(customer=customer)
            order.products.set(request.POST.getlist('product_ids[]'))

            return redirect('order_success')
        else:
            # If customer information is missing, add an error message
            error_message = "Customer information is missing."
            products = Product.objects.all()
            return render(request, 'place_order.html', {'products': products, 'error_message': error_message})
    else:
        products = Product.objects.all()
        return render(request, 'place_order.html', {'products': products})