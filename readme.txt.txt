Comprobar si python instalado:

py --version

Cargar el entorno python:
.\cenv\Scripts\activate

Sino existe, crear uno: 
 py -m venv cenv ->cenv es el nombre a dar  

Mirar si django instalado:
py -m django --version 

Instalar Django si no está:
pip install django 

Ejecutar server:
py manage.py runserver

Si hace falta, instalar django rest api, simplehistory y pillow
pip install djangorestframework
pip install django-simple-history
 pip install Pillow

Entrar al servidor:
http://localhost:8000/user/user/

Post para crear usuarios:
{
  "username": "nuevo_usuario",
  "email": "usuario@example.com",
  "name": "Nombre",
  "last_name": "Apellido",
  "password": "tu_contraseña_segura"
}


Al cambiar el modelo:
python manage.py makemigrations
python manage.py migrate