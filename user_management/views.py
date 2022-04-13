import requests
from rest_framework import status, generics, views,permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from user_management.serializers import PasswordResetSerializer
from .serializers import UserSerializer, EditUserSerializer, CustomUserSerializer
from .models import User, Profile
from drf_yasg.utils import swagger_auto_schema

@api_view(['GET'])
def activate_user_view(request, uid, token):
    post_url = "http://127.0.0.1:8002/api/auth/users/activation/"
    post_data = {"uid": uid, "token": token}
    result = requests.post(post_url, data=post_data)
    content = result.text
    return Response(content)


@api_view(['POST'])
def password_reset_view(request, uid, token):
    data = request.data
    serializer = PasswordResetSerializer(data=data)
    if serializer.is_valid():
        post_url = "http://127.0.0.1:8002/api/auth/users/reset_password_confirm/"
        post_data = {"uid": uid, "token": token, 'new_password': data['password']}
        result = requests.post(post_url, data=post_data)
        content = result.text
        return Response({"content": content, "result": result}, '200')
    else:
        return Response(serializer.errors, '400')



class LogoutAPIView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')
            token_obj = RefreshToken(refresh_token)
            token_obj.blacklist()
            return Response({"message": "Logout Sccessfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Message": "Something Went wrong"}, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = EditUserSerializer


class UpdateManagement(APIView):
    @swagger_auto_schema(
        request_body=CustomUserSerializer,

        responses={
            200: "OK",
            400: "Bad Request",
            500: "Internal Server Error",
        },
    )
    def put(self, request, pk):
        try:
            profile_object = Profile.objects.get(pk=pk)
            serializer = CustomUserSerializer(profile_object)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Profile.DoesNotExist:
            return Response({"message": f" object does not exist against {pk}"}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"message": e.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
