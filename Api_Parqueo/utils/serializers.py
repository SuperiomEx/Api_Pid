from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from ..models import Parqueo, Espacio, Reserva

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['email', 'nombre', 'password', 'token']
        extra_kwargs = {
            'password': {'write_only': True},
            'nombre': {'required': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            nombre=validated_data['nombre'],
            password=validated_data['password']
        )
        return user

    def get_token(self, obj):
        refresh = RefreshToken.for_user(obj)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

class ParqueoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parqueo
        fields = ['id', 'nombre', 'direccion', 'tarifa']


class EspacioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Espacio
        fields = ['id', 'parqueo', 'numero', 'disponible']
        
    def to_representation(self, instance):
        # Muestra el nombre del parqueo en lugar del ID
        representation = super().to_representation(instance)
        representation['parqueo'] = instance.parqueo.nombre
        return representation


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id', 'espacio', 'fecha_inicio', 'fecha_fin', 'pagado']
        extra_kwargs = {
            'pagado': {'read_only': True},
        }

    def validate_espacio(self, value):
        if not value.disponible:
            raise serializers.ValidationError("Este espacio no está disponible")
        return value




