from rest_framework import mixins
from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk' # default

class ProductGenericViewSet(
  mixins.ListModelMixin,
  mixins.RetrieveModelMixin,
  viewsets.GenericViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk' # default
