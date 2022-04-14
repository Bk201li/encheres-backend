from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            "Enpoint": "/products/",
            "method": "GET",
            "body": None,
            "description": "Get all products",
        },
        {
            "Enpoint": "/products/id",
            "method": "GET",
            "body": None,
            "description": "Returns a single product",
        },
        {
            "Enpoint": "/products/create",
            "method": "POST",
            "body": None,
            "description": "Create a product",
        },
    ]

    return Response(routes)

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
