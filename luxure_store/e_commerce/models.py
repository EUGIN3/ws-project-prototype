from django.db import models
from django.contrib.auth.models import User
import datetime


class Category(models.Model):
    name = models.CharField(max_length=200)
	
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default="", blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url


class Order(models.Model):
    transaction_id = models.CharField(max_length=100, null=True)
    customer =  models.ForeignKey(Customer, on_delete=models.CASCADE)
    status =  models.BooleanField(default=False )

    def __str__(self):
        return str(self.transaction_id)
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    

    @property
    def shipping(self):
        return True
    

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date =  models.DateField(default=datetime.datetime.today)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False) 
    zipcode = models.CharField(max_length=200, null=False)
    date =  models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return self.address