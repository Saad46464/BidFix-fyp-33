from user_management.models import User
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Category
from .serializers import CategorySerializer, ProductSerializer
from django.shortcuts import get_object_or_404

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def pre_save(self, obj):
        obj.joining_letter = self.request.FILES.get('file')


def get_queryset(self):
    product_category = self.request.query_params.get('product_category', None)
    parent_id = Category.objects.get(product_category=product_category)
    cats = Category.objects.filter(parent_id=parent_id)

    qs = Product.objects.filter(category_id__in=parent_id)

    print(qs)
    return qs


class CategoryListView(APIView):
    """CategorylistView class

        This view performs list operations for FAQ

        Parameters
        ----------
        APIView : rest_framework.views

        """

    @swagger_auto_schema(
        request_body=CategorySerializer,
        responses={
            200: "OK",
            400: "Bad Request",
            500: "Internal Server Error",
        },
    )
    def post(self, request):
        try:
           serializer = CategorySerializer(data=request.data)
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
            category = Category.objects.all()
            serializer = CategorySerializer(category, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
           return Response({"message": e.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(["GET"])
def product_user(request, pk, *args, **kwargs):
        seller_id = get_object_or_404(User, pk=pk)
        products = Product.objects.filter(seller_id=seller_id)
        serializer = ProductSerializer(products, context={"request": request}, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def product_category(request, pk,*args,**kwargs):
    category = get_object_or_404(Category, pk=pk)
    products =Product.objects.filter(category=category)
    serializer =  ProductSerializer(products,context={"request": request}, many=True)
    return Response(serializer.data)
