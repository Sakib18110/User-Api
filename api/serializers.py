from rest_framework import serializers
from .models import UserProfile, UserHobby, UserAddress
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['name', 'age', 'contact']


class UserHobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHobby
        fields = ['hobby']


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ['address']


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50, write_only=True)

    user_profile = UserProfileSerializer(many=True)
    user_address = UserAddressSerializer(many=True)
    user_hobby = UserHobbySerializer(many=True)

    def create(self, validated_data):
        user_profile = validated_data.pop('user_profile')
        user_address = validated_data.pop('user_address')
        user_hobby = validated_data.pop('user_hobby')

        profile_instance = User.objects.create(**validated_data)

        for profile in user_profile:
            UserProfile.objects.create(user=profile_instance, **profile)

        for address in user_address:
            UserAddress.objects.create(user=profile_instance, **address)

        for hobby in user_hobby:
            UserHobby.objects.create(user=profile_instance, **hobby)

        return profile_instance

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['email', 'first_name', 'last_name', 'username', 'password', 'user_profile',
                  'user_address', 'user_hobby']
        extra_kwargs = {'password': {'write_only': True}}

