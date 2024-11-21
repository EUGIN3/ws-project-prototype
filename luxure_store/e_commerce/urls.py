from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.main, name='main'),

    path("store/", views.store, name='store'),
    path("store/cart/", views.cart, name='cart'),

    path('update_item/', views.updateItem, name="update_item"),
    path('store/cart/address/', views.address, name="address"),
    path('process_order/', views.processOrder, name="process_order"),

    path("store/details/<int:id>", views.details, name='details'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

