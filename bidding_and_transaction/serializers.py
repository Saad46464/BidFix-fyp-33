from rest_framework.serializers import ModelSerializer
from products.models import Product
from products.serializers import ProductSerializer
from .models import Offers, MyCart


class OffersSerializer(ModelSerializer):

    class Meta:
        """Meta class for Serializer OfferSerializer"""
        model = Offers
        fields = '__all__'



class MyCartSerializer(ModelSerializer):

    class Meta:
        """Meta class for Serializer offerSerializer"""
        model = MyCart
        fields = '__all__'




class OfferProductSerializer(ModelSerializer):
    products_detail = OffersSerializer(many=True, read_only=True)
    class Meta:
        """Meta class for Serializer offerSerializer"""
        model = Product
        fields = ('products_detail','id')
    # def to_representation(self, instance):
    #         response = super().to_representation(instance)
            # response['seller'] = f"{instance.seller.first_name}"
            # response['seller'] = f"{instance.products_detail.seller.first_name} "
            # response['buyer'] = f"{instance.buyer.first_name} "
            # return response


class MycartProductSerializer(ModelSerializer):
    productId = ProductSerializer(many=True, read_only=True)
    class Meta:
        """Meta class for Serializer offerSerializer"""
        model = MyCart
        fields = ('productId' , 'id')
