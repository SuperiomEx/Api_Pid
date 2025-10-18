from django.urls import path
from .views.login import *
from .views.register import *
from .views.reserved import *

urlpatterns = [
    path('auth/register/', UserRegistrationAPIView.as_view(), name='register'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('parqueos/', ParqueoListCreateView.as_view(), name='parqueo-list-create'),
    path('espacios/', EspacioListCreateView.as_view(), name='espacio-list-create'),
    path('reservas/', ReservaListView.as_view(), name='reserva-list'),
]