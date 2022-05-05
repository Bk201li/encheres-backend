from django.contrib import admin
from .models import Product, Auction

# Register your models here.

admin.site.register(Product)
admin.site.register(Auction)