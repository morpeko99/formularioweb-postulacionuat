# formularioweb-postulacionuat
Formulario realizado con VueJS, Flask y Mysql.


## Contexto
A modo de postulación a la Unidad de Asistencia Técnica, se solicitó realizar un formulario orientado en el área médica con las siguientes tecnologías:

- Backend
  - Python: Flask o Django
  - PHP: Codeigniter o Laravel
- Frontend
  - VueJs o React
- Persistencia de datos
  - SQL: MySQL o PostgreSQL
  - NoSQL: MongoDB

En este proyecto se seleccionó para el Flask para el Backend, VueJs para el Frontend y MySQL para la base de datos.

## Instalación de dependencias
### Backend
1. Entorno virtual de python
Se debe crear un entorno virtual de python, por lo que se debe debe instalar el paquete virtualenv con el siguiente comando `pip install virtualenv`, con lo anterior listo, ya se puede crear el entorno virtual, por lo que se tipea `python virtualenv <nombre del entorno>` en la carpeta que se quiera iniciar el proyecto. El entorno virtual se activa tipeando en la consola `.\<nombre del entorno>\Script\activate`.

2. Instalación de modulos
Con el entorno virtual activado, se deben instalar los módulos necesarios, con el comando `pip install flask==2.0.2 flask-sqlalchemy==2.5.1 flask-cors==3.0.10 flask-mail==0.9.1 flask-marshmallow==0.14.0 marshmallow-sqlalchemy==0.26.1 pymysql==1.0.2`.

3. Ejecución de API Rest
Para comenzar el uso, se debe crear una base de datos en MySQL (versión 8.0.27), luego editar el archivo `configdb.json` ubicado en la carpeta backend, en este archivo se debe agregar tanto el usuario y contraseña de MySQL y el nombre de la base de datos que se acaba de crear. Con esto y ubicados en la carpeta backend, ya se puede ejecutar con `python ./src/app.py`.
### Frontend
#### Instalación de dependencias  VueJs
Primero se instala nodejs (versión 16.13.0, en este proyecto), para poder utilizar el sistema de gestión de paquetes de node, npm (versión 8.1.3).
1. Se escribe en la consola `npm install webpack -g`.
2. Luego, para instalar vue-cli, se escribe en la consola `npm install vue-cli -g`.
3. Ahora, ingresar a la dirección del proyecto de vue, en este caso a la carpeta llamada websiteuat, con `cd <dirección>\frontend\websiteuat` y escribir `npm install`.
4. con todo lo anterior listo, ya se puede probar con `npm run dev`.

El detalle de la versión de cada paquete está en `package.json`.
