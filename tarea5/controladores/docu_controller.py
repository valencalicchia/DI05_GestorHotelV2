from PySide6.QtWidgets import QDialog

from vistas.ui_documentacion import Ui_Dialog

class DocuController(QDialog):
    def __init__(self):
        """
        Constructor de la clase MainCotroller, que se encarga de gestionar la ventana principal 
        y las interacciones con las reservas de los salones.
        """
        super().__init__()
        self.ui = Ui_Dialog()  # Inicializa la interfaz de usuario
        self.ui.setupUi(self)  # Configura la interfaz en la ventana principal

        html ="""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 10px;
        }
        img {
            max-width: 100%;
        }
        p {
            font-size: 14px;
            line-height: 1.6;
        }
    </style>
</head>
<body>

    <h1>Uso de la App</h1>

    <h2>Primeros pasos</h2>
    <p>Esta app es bastante sencilla de usar, primero debemos indicar los parámetros de conexión, la base de datos y demás:</p>
    <div><img src="../img/conexionbd.png" alt="Conexión a la base de datos"></div>

    <p>Una vez tenemos esto definido, nos aparecerá la pantalla para logarnos con nuestras credenciales de acceso a la aplicación con las credenciales correctas (indicadas en la tarea):</p>
    <div><img src="../img/login.png" alt="Pantalla de login"></div>

    <p>Lo primero que encontramos al entrar es la pantalla principal, la cual nos permitirá acceder a las distintas opciones disponibles:</p>
    <div><img src="../img/menu.png" alt="Menú principal"></div>

    <h2>Gestión de Reservas</h2>

    <p>Si entramos a la opción <strong>"Aplicaciones" -> "Reservas"</strong>, veremos dos recuadros: uno con los salones disponibles y otro con la tabla de las reservas hechas para el salón seleccionado. Si cambiamos de salón, se filtrará por ese criterio:</p>
    <div><img src="../img/reservas.png" alt="Gestión de reservas"></div>

    <p>Tenemos abajo dos opciones: si damos a <strong>"Reservar"</strong>, nos abrirá un formulario desde el cual podremos crear una nueva reserva para el salón seleccionado. Si damos a <strong>"Ver Detalle"</strong>, entraremos en el modo visualización de la reserva:</p>
    <div><img src="../img/reservaview.png" alt="Vista de reserva"></div>

    <p>En este caso, podremos eliminar la reserva seleccionada o, si damos a <strong>"Editar"</strong>, se nos habilitará el modo edición para modificar los datos de la misma:</p>
    <div><img src="../img/reservasedicion.png" alt="Edición de reserva"></div>

    <h2>Gestión de Clientes</h2>

    <p>Si entramos a la opción <strong>"Aplicaciones" -> "Clientes"</strong>, podremos ver la pantalla de gestión de todos los clientes:</p>
    <div><img src="../img/clientes.png" alt="Gestión de clientes"></div>

    <p>De igual forma que con las reservas, si presionamos <strong>"Nuevo"</strong>, se nos abrirá un formulario vacío con el que podremos crear un cliente. Si seleccionamos uno y damos a <strong>"Ver Detalles"</strong>, entraremos en el modo visualización del cliente:</p>
    <div><img src="../img/clienteview.png" alt="Vista de cliente"></div>

    <p>De nuevo, podremos eliminar al cliente seleccionado o, si damos a <strong>"Editar"</strong>, se nos habilitará el modo edición para modificar los datos:</p>
    <div><img src="../img/clienteedit.png" alt="Edición de cliente"></div>

    <p><strong>Y eso sería todo :)</strong></p>

</body>
</html>
"""
        self.ui.textBrowser.setHtml(html)