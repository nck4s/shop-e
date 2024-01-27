from django.shortcuts import render, redirect
from .models import Product, Order, Customer
from django.db import IntegrityError

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})



def add_to_cart(request, product_id):
    # Retrieve or create a list to store selected product IDs in the session
    selected_product_ids = request.session.get('selected_product_ids', [])
    selected_product_ids.append(product_id)
    request.session['selected_product_ids'] = selected_product_ids
    return redirect('product_list')



def place_order(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')

        if customer_name and customer_email:
            customer, created = Customer.objects.get_or_create(
                name=customer_name,
                email=customer_email
            )

            # Retrieve selected product IDs from the session
            selected_product_ids = request.session.get('selected_product_ids', [])
            
            order = Order.objects.create(customer=customer)
            order.products.set(selected_product_ids)

            # Clear the selected product IDs from the session
            request.session['selected_product_ids'] = []

            return redirect('order_success')
        else:
            error_message = "Customer information is missing."
            products = Product.objects.all()
            return render(request, 'place_order.html', {'products': products, 'error_message': error_message})
    else:
        products = Product.objects.filter(id__in=request.session.get('selected_product_ids', []))
        return render(request, 'place_order.html', {'products': products})
    



def view_cart(request):
    # Fetch cart information and pass it to the template
    # For example, you can use the request.session to store cart information
    cart_items = request.session.get('cart', [])
    return render(request, 'view_cart.html', {'cart_items': cart_items})
