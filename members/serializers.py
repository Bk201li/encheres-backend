from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'birth_date', 'phone_number', 'image', 'area', 'created_at', 'updated_at']
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = User.objects.create_user(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance