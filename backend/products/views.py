from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Product
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin
from .serializers import ProductSerializer

# region FIRST WAY YOU CAN BUILD YOUR VIEW

# region CREATE OR LIST PRODUCTS
class ProductListCreateAPIView(
  UserQuerySetMixin,
  StaffEditorPermissionMixin,
  generics.ListCreateAPIView):

  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  def perform_create(self, serializer):
    # serializer.save(user=self.request.user)
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('content') or None
    if content is None:
      content = title
    serializer.save(user=self.request.user, content=content)

  # def get_queryset(self, *args, **kwargs):
  #   qs = super().get_queryset(*args, **kwargs)
  #   request = self.request
  #   return qs.filter(user=request.user)
# endregion

# region PRINT THE PRODUCT DETAILS
class ProductDetailAPIView(
  UserQuerySetMixin,
  StaffEditorPermissionMixin,
  generics.RetrieveAPIView):

  queryset = Product.objects.all()
  serializer_class = ProductSerializer
# endregion

# region UPDATE A PRODUCT
class ProductUpdateAPIView(
  UserQuerySetMixin,
  StaffEditorPermissionMixin,
  generics.UpdateAPIView):

  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk' # default

  def perform_update(self, serializer):
    instance = serializer.save()
    if not instance.content:
      instance.content = instance.title
# endregion

# region DELETE A PRODUCT
class ProductDeleteAPIView(
  UserQuerySetMixin,
  StaffEditorPermissionMixin,
  generics.DestroyAPIView):

  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk' # default

  def perform_destroy(self, instance):
    super().perform_destroy(instance)
# endregion

# endregion

# region SECOND WAY YOU CAN BUILD YOUR VIEW
class ProductMixinView(
  mixins.CreateModelMixin,
  mixins.ListModelMixin,
  mixins.RetrieveModelMixin,
  generics.GenericAPIView):

  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  def get(self, request, *args, **kwargs):
    pk = kwargs.get('pk')
    if pk is not None:
      return self.retrieve(request, *args, **kwargs)
    return self.list(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

  def update(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  def perform_create(self, serializer):
    content = serializer.validated_data.get('content') or None
    if content is None:
      content = 'This is a single view doing cool stuff'
    serializer.save(content=content)
# endregion

# region THIRD WAY YOU CAN BUILD YOUR VIEW
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):

  if request.method == 'GET':
    if pk is not None:
      # Detail View
      obj = get_object_or_404(Product, pk=pk)
      data = ProductSerializer(obj).data
      return Response(data)
    # List View
    queryset = Product.objects.all()
    data = ProductSerializer(queryset, many=True).data
    return Response(data)

  if request.method == 'POST':
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      title = serializer.validated_data.get('title')
      content = serializer.validated_data.get('content') or None
      if content is None:
        content = title
      serializer.save(content=content)
      return Response(serializer.data)
# endregion
