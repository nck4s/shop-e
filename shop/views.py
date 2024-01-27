from django.shortcuts import render, redirect
from .models import Product, Order, Customer


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def place_order(request):
         if request.method == 'POST':
             customer = Customer.objects.create(
                 name=request.POST['customer_name'],
                 email=request.POST['customer_email']
             )
             order = Order.objects.create(customer_name=customer.name)
             order.products.set(request.POST.getlist('product_ids[]'))
             return redirect('order_success')
         else:
             products = Product.objects.all()
             return render(request, 'place_order.html', {'products': products})
        



