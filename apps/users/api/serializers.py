from dataclasses import fields
from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    #Define que campos se van a usar en un update o create
    class Meta: 
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        updated_user = super().update(instance,validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    #Define que campos se van a usar en un listado o detalle
    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password']
        }


"""
class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 40)
    email = serializers.EmailField()

    def validate_email(self,value):
        return value
    
    def validate_name(self,value):
        ### if "g" in value:
        ###    raise serializers.ValidationError('Error, la letra G no está permitida en el nombre.');
        ### return value

    def validate(self,value):
        return value

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.email = validated_data.get('email',instance.email)
        instance.save()
        return instance
    
    ### Esinteresante sobreescibir el metodo save() del serializer
    ### si no queremos que s ejecute el update. Por ejemplo si solo queremos que pase
    ### una validación. 
    ### def save(self):
    ###    send_mail()
    """