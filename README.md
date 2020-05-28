# ServiExpress
_ServiExpress es Nuestro proyecto de Portafolio de Titulo de la carrera Tecnico Analista Programador de DuocUC._\
_Los Integrantes que conforman el equipo de desarrollo son:_\
_Franco Beltrán_\
_Demian Velis_\
_Miguel Rubio_\
_Samuel Fridman_
## Comenzando 🚀
_Las siguientes instrucciones te permitirán hacer uso de nuestro software de gestión con fines de Desarrollo, Pruebas y Evaluación_
### Pre-requisitos 📋
_Para hacer uso de nuestro producto necesitas los siguientes softwares:_
```
Python 3.8.2
```
* [Python 3.8.2](https://www.python.org/downloads/release/python-382/) - Lo puedes descargar aquí

```
Django                        pip install Django==3.0.6
```
* [Django 3.0.6](https://www.djangoproject.com/download/) - Puedes encontrar la documentación de como instalarlo aquí
```
Django Crispy Forms           pip install django-crispy-forms
```
* [Django Crispy Forms 1.9.1](https://django-crispy-forms.readthedocs.io/en/latest/install.html) - Puedes encontrar la documentación de como instalarlo aquí

```
Oracle 18c Express Edition 
```
* [Oracle 18c](https://www.oracle.com/database/technologies/xe-downloads.html) - Lo puedes descargar aquí
```
Oracle Instant Client 32Bits
```
* [Oracle Instant Client 32Bits](https://www.oracle.com/cl/database/technologies/instant-client/microsoft-windows-32-downloads.html) - Lo puedes descargar aquí, debes agregarlo a tus variables de entorno de tu sistema(Path)
```
Cx-oracle 7.3.0               pip install cx_Oracle
```
* [Cx-oracle](https://pypi.org/project/cx-Oracle/) - Puedes encontrar la documentacion aquí
### Instalación 🔧
_Lo primero que debemos hacer es clonar este repositorio para poder tenerlo en nuestra maquina de manera local_

* [ServiExpress](https://github.com/FrancoBeltranQuezada/Portafolio/archive/master.zip) -Lo puedes descargar directo desde aquí
* _Primero debemos crear nuestro usuario con el cual haremos la conexión con la base de datos Oracle 18c, ingresando en la siguiente ruta(preferentemente desde Microsoft Edge,Moxilla o Google Chrome), si nos solicita permitir el uso de flash daremos en Aceptar._
```
https://localhost:5500/em
```
* [localhost:5500](https://localhost:5500/em) - Puedes Acceder directo desde aquí
* _Los datos para loguearnos son_
```
Nombre de Usuario:system
Contraseña:(la clave que pusimos en la instalación de Oracle 18c)
Nombre de Contenedor:(No ingresaremos nada)
No marcar la opción de Como sysdba
```
* _Dentro iremos a la opción de Seguridad/Usuario y crearemos un nuevo usuario_\
*_los datos para ese usuario serán los siguientes:_
```
Nombre:C##DJANGO
Contraseña:django

Tablespace por Defecto: USERS
Tablespace Temporar: TEMP

Privilegios: DBA
```


* _Luego de crear nuestro usuario ir a setting.py de la carpeta **SERVIEXPRESS** de nuestro proyecto de Django y revisar que el puerto en el que se instalo nuestro **Oracle 18c Express Edition** sea el mismo número que esta dentro de DATABASES en el campo 'NAME',**1521** es el puerto por defecto_

```
DATABASES = {
    'default': {
    'ENGINE':   'django.db.backends.oracle',
    'NAME':     'localhost:1521/XE',
    'USER':     'C##DJANGO',
    'PASSWORD': 'django',
    
  }}
```
* _Luego de realizar la configuración de nuestra base de datos procederemos a correr el servidor de nuestro proyecto, para ello debemos abrir nuestro CMD e ir a la ruta donde clonamos nuestro repositorio, en ella activaremos nuestro ambiente virtual con el siguiente comando:_
```
C:\Portafolio\amb\Scripts>activate
```
* _Una vez activado el ambiente virtual volveremos a la carpeta inicial donde se encuentra el archivo **manage.py** y procederemos a crear un superusuario con el comando:_

```
python manage.py createsuperuser
```

* _Ahora debemos hacer nuestras migraciones de los modelos de **django** a nuestra base de datos **Oracle 18c** con los siguientes comandos_
```
python manage.py makemigrations
python manage.py migrate
```

* _Luego de crear nuestro superusuario y hacer nuestras migraciones podremos correr nuestro servidor del proyecto, para ello debemos ejecutar el comando:_
```
python manage.py runserver
```
* _Al iniciar nuestro servidor este nos proveera una ruta para poder acceder al proyecto web a través de nuestro navegador dentro del siguiente mensaje:_
```
System check identified no issues (0 silenced).
May 27, 2020 - 21:42:44
Django version 3.0.6, using settings 'SERVIEXPRESS.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
* [http://127.0.0.1:8000/](http://127.0.0.1:8000/) - Puedes Acceder directo desde aquí
* _Una vez dentro ya puedes comenzar a utilizar el software de gestión de **ServiExpress**_
