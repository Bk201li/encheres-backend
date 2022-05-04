from rest_framework.serializers import ModelSerializer
from .models import Product, Auction

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class AuctionSerializer(ModelSerializer):
    class Meta:
        model = Auction
        fields = '__all__'