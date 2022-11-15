from rest_framework import serializers

class UserProductInlineSrializer(serializers.Serializer):
  detail_url = serializers.HyperlinkedIdentityField(view_name='product-detail', read_only=True)
  title = serializers.CharField(read_only=True)

class UserPublicSerializer(serializers.Serializer):
  username = serializers.CharField(read_only=True)
  id = serializers.IntegerField(read_only=True)
  # other_products = serializers.SerializerMethodField(read_only=True)

  # def get_other_products(self, obj):
  #   user = obj
  #   my_products_qs = user.product_set.all()[:5]
  #   return UserProductInlineSrializer(my_products_qs, many=True, context=self.context).data
