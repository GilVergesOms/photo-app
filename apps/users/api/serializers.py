from dataclasses import fields
from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = '__all__'

class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 40)
    email = serializers.EmailField()

    def validate_email(self,value):
        return value
    
    def validate_name(self,value):
        if "g" in value:
            raise serializers.ValidationError('Error, la letra G no está permitida en el nombre.');
        return value

    def validate(self,value):
        return value

    def create(self, validated_data):
        return User.objects.create(**validated_data)
        