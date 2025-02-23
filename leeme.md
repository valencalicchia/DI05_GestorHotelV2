# Tarea 5 DI - Valentina Alessandra Calicchia

Esta tarea es el desarrollo de un Gestor de Reservas para un hotel. Se ha realizado con Python, PySide6 y MySql. A través de este gestor, el usuario puede crear y modificar reservas de los distintos salones disponibles de un hotel.

Para poner a correr el código debemos seguir estos pasos:

1. Vamos a la ruta de proyecto, instalamos las dependencias:

> pip install -r requirements.txt

2. Levantamos el contenedor para la base de datos:

> docker compose up


3. Ejecutamos el archivo main.py

# Distribución de la app

Para la distribución de esta app he decidido crear un ejecutable, para esto, creamos el archivo [tarea5.py](/tarea5.py), el cual nos servirá como puente para la ejecución.

Una vez lo tenemos, con el paquete pyinstaller, ejecutamos el comando  pyinstaller --onefile --windowed
tarea5.py, el cual nos generará el ejecutable en la carpeta dist:

![conexionbd](img/cmd.png)
![conexionbd](img/exec.png)

# Uso de la App

## Primeros pasos

Esta app es bastante sencilla de usar, primero debemos indicar los parametros de conexión, la base de datos y demás:

![conexionbd](img/conexionbd.png)

Una vez tenemos tenemos esto definido, nos aparecerá la pantalla para logarnos con nuestras credenciales de acceso a la aplicación con las credenciales correctas (indicadas en la tarea):

![login](img/login.png)

Lo primero que encontramos el entrar es la pantalla principal, la cual nos permitirá acceder a las distintas opciones disponibles:

![menu](img/menu.png)

## Gestión de Reservas

Si entramos a la opción "Aplicaciones" -> "Reservas", ahí, veremos dos recuadros, uno con los salones disponibles y otro con la tabla de las reservas hechas para el salón seleccionado, si cambiamos de salón, se filtrará por ese criterio:

![reservas](img/reservas.png)

Tenemos abajo dos opciones, si damos a "Reservar" nos abrirá un formulario desde el cual podremos crear una nueva reserva para el salón que tengamos seleccionado, si damos a "Ver Detalle", entraremos en el modo visualización de la reserva:

![reservaview](img/reservaview.png)

En este caso, podremos bien Eliminar la reserva seleccionada o, si damos a "Editar" se nos habilita el modo edición para modificar los datos de la misma:

![reservasedicion](img/reservasedicion.png)

## Gestión de Clientes

Si entramos a la opción "Aplicaciones" -> "Clientes" podremos ver la pantalla de gestión de todos los clientes:

![clientes](img/clientes.png)

De igual forma que con las reservas, si presionamos "Nuevo", se nos abrirá un formulario vacío con el que podremos crear un cliente y si seleccionamos uno y damos a "Ver Detalles", entraremos en el modo visualización del cliente:

![reservaview](img/clienteview.png)

De nuevo, podremos bien Eliminar al cliente seleccionada o, si damos a "Editar" se nos habilita el modo edición para modificar los datos:

![reservasedicion](img/clienteedit.png)

Y eso sería todo :)