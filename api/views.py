from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product


@api_view(["GET"])
def get_routes(request):
    routes = [
        {
            "Enpoint": "/token/",
            "method": "GET",
            "body": None,
            "description": "Get the refresh and acess tokens",
        },
        {
            "Enpoint": "/token/refresh/",
            "method": "POST",
            "body": None,
            "description": "Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid.",
        },
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
        {
            "Enpoint": "/members/register",
            "method": "POST",
            "body": {"email": "", "password": ""},
            "description": "Register a user",
        },
        {
            "Enpoint": "/members/user",
            "method": "GET",
            "body": None,
            "description": "Returns the current user",
        },
    ]

    return Response(routes)


@api_view(["GET"])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_product(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def create_product(request):
    data = request.data

    product = Product.objects.create(
        body=data["body"],
    )
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
def update_product(request, pk):
    data = request.data

    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, data=request.POST)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response("Product deleted successfully")
