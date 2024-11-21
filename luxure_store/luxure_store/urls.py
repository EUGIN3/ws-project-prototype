from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('e_commerce.urls')),
    path("admin/", admin.site.urls),
]
