from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view(['GET', 'POST'])
def api_home(request, *args, **kwargs):

  if request.method == 'GET':
    instance = Product.objects.all().order_by("?").first()
    data = {}

    if instance:
      data = ProductSerializer(instance).data

    return Response(data)

  elif request.method == 'POST':
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
      # instance = serializer.save()
      print(serializer.data)
      return Response(serializer.data)
