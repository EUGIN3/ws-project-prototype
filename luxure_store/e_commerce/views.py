from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
import datetime

from .models import *


def main(request):
    context = {}
    return render(request, 'main.html', context)


def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, status=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {
            'get_cart_items' : 0,
            'get_cart_total' : 0,
            'shipping' : False
        }
        cartItems = order['get_cart_items']

    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories' : categories,
        'products' : products,
        'cartitems' : cartItems
    }
    return render(request, 'store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, status=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {
            'get_cart_items' : 0,
            'get_cart_total' : 0,
            'shipping' : False
        }
        cartItems = order['get_cart_items']

    context = {
        'items' : items,
        'order' : order,
        'cartitems' : cartItems
    }
    return render(request, 'cart.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, status=False)
    
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
         orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def address(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, status=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {
            'get_cart_items' : 0,
            'get_cart_total' : 0,
            'shipping' : False
        }
        cartItems = order['get_cart_items']

    context = {
        'items' : items,
        'order' : order,
        'cartitems' : cartItems
    }

    return render(request, 'shipping.html', context)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, status=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.status = True
        order.save()

        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            zipcode=data['shipping']['zipcode'],
        )
    else:
        print('User is not logged in')
          
    return JsonResponse('Payment submitted..', safe=False)


def details(request, id):
    product = Product.objects.get(id=id)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, status=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {
            'get_cart_items' : 0,
            'get_cart_total' : 0,
            'shipping' : False
        }
        cartItems = order['get_cart_items']

    context = {
        'product' : product,
        'cartitems' : cartItems
    }
          
    return render(request, 'details.html', context)



