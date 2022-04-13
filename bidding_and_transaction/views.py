from django.db.models import F
from django.http.response import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import OffersSerializer, MyCartSerializer, OfferProductSerializer, MycartProductSerializer


class OffersView(APIView):
    """offersView class

        This view performs GET,PUT and DELETE operations for FAQ

        Parameters
        ----------
        APIView : rest_framework.views

        """
    def get(self, request, pk):
        try:
            offers_object = Offers.objects.get(pk=pk)
            serializer = OffersSerializer(offers_object)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Offers.DoesNotExist:
             return Response({"message": f"nft object does not exist against {pk}"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
           return Response({"message": e.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    @swagger_auto_schema(
        request_body=OffersSerializer,

        responses={
            200: "OK",
            400: "Bad Request",
            500: "Internal Server Error",
        },
    )
    def put(self, request, pk):
        try:
            offers_object = Offers.objects.get(pk=pk)
            serializer = OffersSerializer(offers_object)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Offers.DoesNotExist:
            return Response({"message": f" object does not exist against {pk}"}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"message": e.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(
        responses={
            200: "OK",
            400: "Bad Request",
            500: "Internal Server Error",
        },
    )
    def delete(self, request, pk):
        try:
            offers = Offers.objects.get(pk=pk)
            offers.delete()
            return Response({"message": "deleted successfully"},status=status.HTTP_200_OK)
        except Offers.DoesNotExist:
            return Response({"message": f"nft object does not exist against {pk}"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": e.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class OffersListView(APIView):
    """OfferslistView class

        This view performs list operations for FAQ

        Parameters
        ----------
        APIView : rest_framework.views

        """

    @swagger_auto_schema(
        request_body=OffersSerializer,
        responses={
            200: "OK",
            400: "Bad Request",
            500: "Internal Server Error",
        },
    )
    def post(self, request):
        try:
           serializer = OffersSerializer(data=request.data)
           if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
           else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
             return Response({"message": e.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MyCartListView(APIView):
    """CategoryistView class

        This view performs list operations for FAQ

        Parameters
        ----------
        APIView : rest_framework.views

        """

    @swagger_auto_schema(
        request_body=MyCartSerializer,
        responses={
            200: "OK",
            400: "Bad Request",
            500: "Internal Server Error",
        },
    )
    def post(self, request):
        try:
           serializer = MyCartSerializer(data=request.data)
           if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
           else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
             return Response({"message": e.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    @swagger_auto_schema(
        responses={
            200: "OK",
            400: "Bad Request",
            500: "Internal Server Error",
        },
    )
    def get(self, request, format=None):
        try:
            mycart = MyCart.objects.all()
            serializer = MyCartSerializer(mycart, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
           return Response({"message": e.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class OfferProductListView(generics.RetrieveAPIView):

             queryset = Product.objects.all()
             serializer_class = OfferProductSerializer


class MycartProductListView(generics.RetrieveAPIView):
    queryset = MyCart.objects.all()
    serializer_class = MycartProductSerializer


@api_view(["GET"])
def product_offers(request, pk,*args,**kwargs):
        try:

            product_offer = Product.objects.filter(pk=pk).annotate(
                seller_name = F('products_detail__seller__first_name'),
                buyer_name = F('products_detail__buyer__first_name'),
                is_ofered = F('products_detail__is_ofered'),
                status=F('products_detail__status'),
                new_price = F('products_detail__new_price'),
            ).values('title','seller_name','buyer_name','is_ofered','status', 'new_price')
            return Response({'product_offer':product_offer}, status=status.HTTP_200_OK)


        except Product.DoesNotExist:
            return Response({"message": f"user object does not exist against {pk}"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"message": e.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
