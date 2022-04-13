from rest_framework.serializers import ModelSerializer
from .models import Category, Product


class CategorySerializer(ModelSerializer):

    class Meta:
        """Meta class for Serializer OfferSerializer"""
        model = Category
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    # product_images = ProductFileSerializer(many=True, read_only=False)
    class Meta:
        """Meta class for Serializer offerSerializer"""
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['category'] = f"{instance.category.name}"
        response['seller_name'] = f"{instance.seller_name.first_name} {instance.seller_name.last_name}"
        return response


class CategoryProductSerializer(ModelSerializer):
    product_category = ProductSerializer(many=True, read_only=True)
    class Meta:
        """Meta class for Serializer OfferSerializer"""
        model = Category
        fields = ('product_category', 'name')
