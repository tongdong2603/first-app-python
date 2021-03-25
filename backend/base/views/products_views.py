from django.contrib.auth.models import User
from rest_framework.response import Response
from ..models import Product
from ..products import products
from ..serializers import ProductSerializer

# permission
from rest_framework.decorators import api_view


@api_view(['GET'])
def getProducts(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    product = None
    for i in products:
        if i['_id'] == pk:
            product = i
            break
    return Response(product)
