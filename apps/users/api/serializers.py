from dataclasses import fields
from rest_framework import serializers
from apps.users.models import User, OTPCode
from apps.users.utils.utils import * # Importa la función de generación de OTP
import re

class UserSerializer(serializers.ModelSerializer):
    #Define que campos se van a usar en un update o create
    class Meta: 
        model = User
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    #Define que campos se van a usar en un listado o detalle
    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email']
        }

class AdvancedUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(max_length=40)
    email = serializers.EmailField()
    name = serializers.CharField(max_length=40)
    last_name = serializers.CharField(max_length=80)
    id = serializers.ReadOnlyField() 

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'last_name', 'password']

    def validate_username(self, value):
        value = value.strip()
        if len(value) < 5:
            raise serializers.ValidationError("El username debe tener mínimo 5 caracteres.")
        if len(value) > 40:
            raise serializers.ValidationError("El nombre de usuario no debe superar los 40 caracteres.")
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Este nombre de usuario ya está registrado.")
        return value

    def validate_email(self, value):
        value = value.strip().lower()
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este correo electrónico ya está registrado.")
        return value

    def validate_name(self, value):
        value = value.strip()
        if len(value) < 2:
            raise serializers.ValidationError("El nombre debe tener mínimo 2 caracteres.")
        if len(value) > 40:
            raise serializers.ValidationError("El nombre no debe superar los 40 caracteres.")
        if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s'-]+$", value):
            raise serializers.ValidationError("El nombre contiene caracteres inválidos.")
        return value

    def validate_last_name(self, value):
        value = value.strip()
        if len(value) < 2:
            raise serializers.ValidationError("Los apellidos deben tener mínimo 2 caracteres.")
        if len(value) > 80:
            raise serializers.ValidationError("Los apellidos no deben superar los 80 caracteres.")
        if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s'-]+$", value):
            raise serializers.ValidationError("Los apellidos contienen caracteres inválidos.")
        return value
    
    def validate_password(self, value):
        # Al menos 8 caracteres, una mayúscula, una minúscula y un dígito
        if len(value) < 8:
            raise serializers.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not re.search(r"[A-Z]", value):
            raise serializers.ValidationError("La contraseña debe contener al menos una letra mayúscula.")
        if not re.search(r"[a-z]", value):
            raise serializers.ValidationError("La contraseña debe contener al menos una letra minúscula.")
        if not re.search(r"[0-9]", value):
            raise serializers.ValidationError("La contraseña debe contener al menos un número.")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        create_otp(user)  # Genera y guarda el OTP al crear el usuario
        return user
