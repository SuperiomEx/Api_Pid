# 🅿️ API de Sistema de Parqueo

Una API REST desarrollada en Django para la gestión de espacios de parqueo, que permite a los usuarios registrarse, autenticarse y reservar espacios de estacionamiento de manera eficiente.

## 📝 Descripción

Este proyecto nació de la necesidad de digitalizar y optimizar la gestión de parqueaderos. La API permite administrar múltiples parqueaderos, sus espacios disponibles y las reservas de los usuarios de forma centralizada. Es ideal para centros comerciales, edificios corporativos o cualquier establecimiento que requiera un sistema de reservas de parqueo.

## ✨ Características

- **Autenticación JWT**: Sistema seguro de autenticación con tokens de acceso y refresh
- **Gestión de usuarios**: Registro y login con validación de credenciales
- **Administración de parqueaderos**: CRUD completo para parqueaderos con información de tarifas
- **Control de espacios**: Gestión de espacios individuales con estado de disponibilidad
- **Sistema de reservas**: Reserva de espacios con validación de horarios y disponibilidad
- **Documentación automática**: Swagger UI y ReDoc integrados
- **Validaciones robustas**: Prevención de reservas superpuestas y validación de fechas

## 🛠️ Tecnologías Utilizadas

- **Django 5.2.1**: Framework web principal
- **Django REST Framework**: Para la creación de la API REST
- **Simple JWT**: Manejo de autenticación con tokens JWT
- **drf-yasg**: Generación automática de documentación de la API
- **SQLite**: Base de datos (fácil migración a PostgreSQL/MySQL)

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

### Instalación paso a paso

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/API_Pid.git
   cd API_Pid
   ```

2. **Crear y activar entorno virtual**
   ```bash
   python -m venv venv
   
   # En Windows
   venv\Scripts\activate
   
   # En macOS/Linux
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install django djangorestframework djangorestframework-simplejwt drf-yasg
   ```

4. **Ejecutar migraciones**
   ```bash
   python manage.py migrate
   ```

5. **Crear superusuario (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar el servidor**
   ```bash
   python manage.py runserver
   ```

¡La API estará disponible en `http://localhost:8000`!

## 📚 Documentación de la API

### Endpoints Principales

#### Autenticación
- `POST /api/auth/register/` - Registro de nuevos usuarios
- `POST /api/auth/login/` - Inicio de sesión y obtención de tokens

#### Parqueaderos
- `GET /api/parqueos/` - Listar todos los parqueaderos
- `POST /api/parqueos/` - Crear nuevo parqueadero (requiere autenticación)

#### Espacios
- `GET /api/espacios/` - Listar espacios disponibles
- `POST /api/espacios/` - Crear nuevo espacio (requiere autenticación)

#### Reservas
- `GET /api/reservas/` - Listar reservas del usuario actual
- `POST /api/reservas/` - Crear nueva reserva (requiere autenticación)

### Documentación Interactiva

Visita estos enlaces una vez que el servidor esté ejecutándose:

- **Swagger UI**: http://localhost:8000/swagger/
- **ReDoc**: http://localhost:8000/redoc/

## 💾 Modelos de Datos

### Usuario
- Email (único)
- Nombre
- Contraseña (encriptada)
- Estado activo
- Fecha de registro

### Parqueo
- Nombre del establecimiento
- Dirección física
- Tarifa por hora/período

### Espacio
- Número identificador
- Parqueo al que pertenece
- Estado de disponibilidad

### Reserva
- Usuario que reserva
- Espacio reservado
- Fecha y hora de inicio
- Fecha y hora de fin
- Estado de pago

## 🔒 Autenticación

La API utiliza JWT (JSON Web Tokens) para la autenticación. Después de un login exitoso, recibirás:

- **Access Token**: Token de corta duración (5 minutos) para acceder a endpoints protegidos
- **Refresh Token**: Token de larga duración (1 día) para obtener nuevos access tokens

### Ejemplo de uso

```bash
# Registro
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"email": "usuario@ejemplo.com", "nombre": "Usuario Ejemplo", "password": "contraseña123"}'

# Login
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email": "usuario@ejemplo.com", "password": "contraseña123"}'

# Usar token en requests autenticados
curl -X GET http://localhost:8000/api/reservas/ \
  -H "Authorization: Bearer TU_ACCESS_TOKEN"
```

## 🧪 Testing

Para ejecutar las pruebas (cuando estén implementadas):

```bash
python manage.py test
```

## 📁 Estructura del Proyecto

```
API_Pid/
├── Api_Parqueo/              # App principal
│   ├── models.py             # Modelos de datos
│   ├── urls.py              # URLs de la app
│   ├── views/               # Vistas organizadas por módulo
│   │   ├── login.py         # Autenticación
│   │   ├── register.py      # Registro de usuarios
│   │   └── reserved.py      # Gestión de reservas
│   └── utils/
│       └── serializers.py   # Serializadores DRF
├── API_Pid/                 # Configuración del proyecto
│   ├── settings.py          # Configuraciones
│   └── urls.py             # URLs principales
└── manage.py               # Script de gestión de Django
```

## 🤝 Contribución

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -m 'Agrega nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## 📋 TODO / Mejoras Futuras

- [ ] Implementar sistema de pagos
- [ ] Agregar notificaciones por email
- [ ] Crear dashboard administrativo
- [ ] Implementar reservas recurrentes
- [ ] Agregar sistema de calificaciones
- [ ] Integración con mapas para ubicación de parqueaderos
- [ ] App móvil complementaria
- [ ] Reportes y analytics avanzados

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**Anthoan de Jesus Linea Perez**

- GitHub: [@tu-usuario](https://github.com/tu-usuario)
- Email: contact@parqueo.local

## 🙏 Agradecimientos

- A la comunidad de Django por su excelente framework
- A Django REST Framework por simplificar la creación de APIs
- A todos los que han contribuido con feedback y sugerencias

---

*¿Tienes alguna pregunta o sugerencia? ¡No dudes en abrir un issue o contactarme directamente!* 🚗💨
