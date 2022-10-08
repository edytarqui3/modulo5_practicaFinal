# README #
### integrantes
* Elmer Mamani Ticona
* Edy Felix Tarqui Guarachi

Este README, cuenta con los pasos para levantar en ambientes de desarrollo la App de farmapp, desarrollado con Python v3.9 y Django v4.1.2

## APP DE MEDICAMENTOS ##
### Requisitos ###

* Python 3.9.6 o superior

### Pasos ###

* Crear entorno virtual
```commandline
virtualenv venv
```
* Instalar los requirements para la App.
```commandline
pip install -r requirements.txt
```
* Correr la App 
```commandline
python manage.py runserver
```
### Usuario de prueba ###
```commandline
username: admin
password: farmapp
```
### Url de acceso en el Navegador
```commandline
http://localhost:8000/farmapp
```
### Django REST Framework
* EndPoint Tipo de Productos
```commandline
Method: [GET]
Url: http://localhost:8000/api/producto/tipoproducto/
Response:
[
    {
        "id": 1,
        "tipoproducto": "MEDICAMENTOS",
        "descripcion": "MEDICAMENTOS"
    },
    {
        "id": 2,
        "tipoproducto": "pastillas",
        "descripcion": "pastillas"
    },
    {
        "id": 3,
        "tipoproducto": "jeringas",
        "descripcion": "jeringas"
    }
]
```
* EndPoint Categoria de productos
```commandline
Method: [GET]
Url: http://localhost:8000/api/producto/categoria/
Response:
[
    {
        "id": 1,
        "categoria": "paracetamol",
        "descripcion": "paraceltamol"
    },
    {
        "id": 2,
        "categoria": "complejo b",
        "descripcion": "complejo b"
    }
]
```
