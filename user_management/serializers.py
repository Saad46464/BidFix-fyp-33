from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken ,TokenError
from djoser.serializers import UserSerializer, UserCreatePasswordRetypeSerializer
from django.db import IntegrityError
from .models import *

class PasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)


class EditUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ('first_name', 'last_name','phone_number','bio','image')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class CustomUserSerializer(UserSerializer):
    user_profile = ProfileSerializer(required=True)

    class Meta(UserSerializer.Meta):
        Model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'user_profile')
        read_only_fields = ('email',)

    def update(self, instance: User, validated_data):
        profile = validated_data('user_profile')
        if len(profile) > 0:
            profile = profile[0]
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.username = validated_data['username']
        instance.save()
        if Profile.objects.filter(user=instance).count() == 0:
            Profile.objects.create(**profile, user=instance)
        else:
            Profile.objects.filter(user=instance).update(**profile)
        return instance


class CreateUserSerializer(UserCreatePasswordRetypeSerializer):

    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
            Profile.objects.create(user=user, bio="bio")
        except IntegrityError:
            self.fail("cannot_create_user")
        return user
