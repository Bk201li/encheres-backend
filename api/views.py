from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product


@api_view(["GET"])
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
        {
            "Enpoint": "/products/id/update",
            "method": "PUT",
            "body": None,
            "description": "Update a product",
        },
        {
            "Enpoint": "/products/id/delete",
            "method": "DELETE",
            "body": None,
            "description": "Delete a product",
        },
    ]

    return Response(routes)


@api_view(["GET"])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def createProduct(request):
    data = request.data

    product = Product.objects.create(
        body=data["body"],
    )
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(["PUT"])
def updateProduct(request, pk):
    data = request.data

    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, data=request.POST)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(["DELETE"])
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response("Product deleted successfully")
