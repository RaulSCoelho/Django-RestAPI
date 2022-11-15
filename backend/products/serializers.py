from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer
from .validators import validate_title_no_hello, unique_product_title
from .models import Product

class ProductInlineSrializer(serializers.Serializer):
  detail_url = serializers.HyperlinkedIdentityField(view_name='product-detail', read_only=True)
  title = serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
  owner = UserPublicSerializer(source='user', read_only=True)
  my_discount = serializers.SerializerMethodField(read_only=True)
  detail_url = serializers.HyperlinkedIdentityField(view_name='product-detail')
  edit_url = serializers.SerializerMethodField(read_only=True)
  title = serializers.CharField(validators=[validate_title_no_hello, unique_product_title])
  # email = serializers.EmailField(source='user.email', read_only=True)
  # related_products = ProductInlineSrializer(source='user.product_set.all', read_only=True, many=True)
  class Meta:
    model = Product
    fields = [
      'owner',
      'detail_url',
      'edit_url',
      'id',
      'title',
      'content',
      'price',
      'sale_price',
      'my_discount',
      'public',
      # 'email',
      # 'related_products'
    ]

  def get_edit_url(self, obj):
    return get_url(self, obj, 'product-update')

  def get_my_discount(self, obj):
    if not hasattr(obj, 'id'):
      return None
    if not isinstance(obj, Product):
      return None
    return obj.get_discount()

  # def validate_title(self, value):
  #   request = self.context.get('request')
  #   user = request.user
  #   qs = Product.objects.filter(user=user, title__iexact=value)
  #   if qs.exists():
  #     raise serializers.ValidationError(f"{value} is already a product name.")
  #   return value

def get_url(self, obj, url_name):
  request = self.context.get('request')
  if request is None:
    return None

  return reverse(url_name, kwargs={'pk': obj.pk}, request=request)
