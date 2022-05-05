from django.db import models
from members.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    color = models.CharField(max_length=255, default="white")
    image = models.ImageField(upload_to="product-images/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-updated_at"]

class Auction(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    end = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name
        
    class Meta:
        ordering = ["-updated_at"]
