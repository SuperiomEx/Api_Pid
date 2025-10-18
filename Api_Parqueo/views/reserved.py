from rest_framework import generics, permissions
from rest_framework.response import Response
from ..models import Parqueo, Espacio, Reserva
from ..utils.serializers import *

# Vista para listar parqueos
class ParqueoListView(generics.ListAPIView):
    queryset = Parqueo.objects.all()
    serializer_class = ParqueoSerializer
    permission_classes = [permissions.AllowAny]

# Vista para buscar espacios disponibles
class EspacioDisponibleView(generics.ListAPIView):
    serializer_class = EspacioSerializer
    
    def get_queryset(self):
        parqueo_id = self.request.query_params.get('parqueo')
        return Espacio.objects.filter(disponible=True, parqueo_id=parqueo_id)

# Vista para crear reservas
class CrearReservaView(generics.CreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        espacio = serializer.validated_data['espacio']
        espacio.disponible = False
        espacio.save()
        serializer.save(usuario=self.request.user)

class ParqueoListCreateView(generics.ListCreateAPIView):
    queryset = Parqueo.objects.all()
    serializer_class = ParqueoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()  # Crea un nuevo parqueo

class EspacioListCreateView(generics.ListCreateAPIView):
    queryset = Espacio.objects.all()
    serializer_class = EspacioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()  # Crea un nuevo espacio

class ReservaListView(generics.ListAPIView):
    serializer_class = ReservaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Solo muestra las reservas del usuario actual
        return Reserva.objects.filter(usuario=self.request.user)

class ReservaCreateView(generics.CreateAPIView):
    serializer_class = ReservaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        espacio_id = serializer.validated_data['espacio'].id
        fecha_inicio = serializer.validated_data['fecha_inicio']
        fecha_fin = serializer.validated_data['fecha_fin']
        
        # Validar que el espacio esté disponible
        espacio = Espacio.objects.get(id=espacio_id)
        if not espacio.disponible:
            return Response(
                {"error": "Este espacio no está disponible"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Validar que las fechas sean correctas
        if fecha_inicio >= fecha_fin:
            return Response(
                {"error": "La fecha de fin debe ser posterior a la de inicio"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if fecha_inicio < timezone.now():
            return Response(
                {"error": "No se puede reservar en fechas pasadas"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Validar que no haya reservas superpuestas
        reservas_existentes = Reserva.objects.filter(
            espacio=espacio,
            fecha_fin__gt=fecha_inicio,
            fecha_inicio__lt=fecha_fin
        ).exists()
        
        if reservas_existentes:
            return Response(
                {"error": "El espacio ya está reservado en ese horario"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Crear la reserva
        reserva = serializer.save(usuario=request.user)
        
        # Marcar el espacio como no disponible
        espacio.disponible = False
        espacio.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)