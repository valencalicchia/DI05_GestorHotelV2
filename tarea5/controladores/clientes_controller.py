from PySide6.QtWidgets import QAbstractItemView, QDialog, QHeaderView
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtCore import QModelIndex

from vistas.clientes_ui import Ui_Clientes
from modelos.datos import ClientesDAO
from controladores.cliente_create_edit_controller import ClienteController
from utilidades.message_box import MessageBox

class ClientesController(QDialog):
    """
    Controlador de la interfaz para gestionar clientes. Esta clase se encarga de manejar la interacción con la
    UI, los eventos, y la lógica asociada a la gestión de clientes.
    """
    
    def __init__(self):
        """
        Constructor de la clase, inicializa la interfaz de usuario y configura los eventos necesarios.
        """
        super().__init__()  # Llama al constructor de la clase base QDialog
        self.ui = Ui_Clientes()  # Instancia la UI de los clientes
        self.ui.setupUi(self)  # Configura la interfaz de usuario
        self.init_ui()  # Llama al método para inicializar la UI y los eventos

    def init_ui(self):
        """
        Método para configurar la interfaz de usuario y los eventos.
        """
        try:
            self.config_events()  # Configura los eventos de la UI
            self.config_table()  # Configura la tabla de clientes
        except Exception as e:
            # En caso de error, se muestra un mensaje de error con la descripción
            MessageBox("Error al configurar la UI", "error", str(e)).show()

    def config_events(self):
        """
        Configura los eventos de la interfaz de usuario, como los clics en los botones.
        """
        # Conecta los botones a sus respectivas funciones
        self.ui.vcGridClientes.clicked.connect(self.click_cliente)  # Evento de clic en la tabla de clientes
        self.ui.vcbtnModificar.clicked.connect(lambda: self.open_modal(False))  # Evento de clic en "Modificar"
        self.ui.vcbtnNuevo.clicked.connect(lambda: self.open_modal(True))  # Evento de clic en "Nuevo"

    def config_table(self):
        """
        Configura la tabla que muestra los clientes.
        """
        self.dao_cliente = ClientesDAO()  # Crea la instancia de acceso a los datos de los clientes
        self.cliente_seleccionado = 0  # Inicializa el cliente seleccionado a 0 (ningún cliente seleccionado)
        
        headers = ["Nombre", "Apellidos", "DNI", "Teléfono", "Id"]  # Encabezados de las columnas de la tabla

        # Obtiene la lista de clientes desde la base de datos
        clientes = self.dao_cliente.get_all()

        # Crea un modelo de tabla con el número de filas y columnas correspondientes
        self.model = QStandardItemModel(len(clientes), len(headers))
        self.model.setHorizontalHeaderLabels(headers)  # Configura los encabezados de las columnas

        # Rellena la tabla con los datos de los clientes
        for row, cliente in enumerate(clientes):
            self.model.setItem(row, 0, QStandardItem(cliente.nombre))  # Columna de "Nombre"
            self.model.setItem(row, 1, QStandardItem(cliente.apellidos))  # Columna de "Apellidos"
            self.model.setItem(row, 2, QStandardItem(cliente.num_identificacion))  # Columna de "DNI"
            self.model.setItem(row, 3, QStandardItem(cliente.telefono))  # Columna de "Teléfono"
            self.model.setItem(row, 4, QStandardItem(str(cliente.id)))  # Columna de "Id" (oculta)

        # Configura el modelo en la tabla de la UI
        self.ui.vcGridClientes.setModel(self.model)
        self.ui.vcGridClientes.setColumnHidden(4, True)  # Oculta la columna de "Id"
        self.ui.vcGridClientes.resizeColumnsToContents()  # Ajusta el tamaño de las columnas automáticamente
        self.ui.vcGridClientes.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # Estira las columnas
        self.ui.vcGridClientes.horizontalHeader().setMinimumSectionSize(100)  # Define el tamaño mínimo de las columnas
        self.ui.vcGridClientes.horizontalHeader().setStretchLastSection(True)  # Estira la última columna
        self.ui.vcGridClientes.verticalHeader().setMinimumSectionSize(35)  # Ajusta el tamaño mínimo de las filas
        self.ui.vcGridClientes.setSelectionBehavior(QAbstractItemView.SelectRows)  # Permite seleccionar filas completas
        self.ui.vcGridClientes.setSelectionMode(QAbstractItemView.SingleSelection)  # Permite solo una selección a la vez

        # Deshabilita la edición de la tabla
        self.ui.vcGridClientes.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

    def open_modal(self, nueva: bool):
        """
        Abre un modal para la creación o modificación de un cliente.
        
        :param nueva: Si es True, abre el modal para crear un nuevo cliente. Si es False, abre el modal para modificar el cliente seleccionado.
        """
        # Si no se ha seleccionado un cliente o es una nueva entrada, abre el modal adecuado
        if self.cliente_seleccionado != 0 or nueva:
            # Si es un nuevo cliente, crea un nuevo controlador
            if nueva:
                self.controlador = ClienteController(None)
            else:
                # Si se va a modificar un cliente, pasa el ID del cliente seleccionado
                self.controlador = ClienteController(self.cliente_seleccionado)

            # Verifica que el controlador sea un QDialog
            if not isinstance(self.controlador, QDialog):
                raise TypeError(
                    "El controlador debe heredar de QDialog para ser modal."
                )
            
            # Establece el modal y lo muestra
            self.controlador.setModal(True)
            self.controlador.finished.connect(self.config_table)  # Al terminar el modal, actualiza la tabla
            self.controlador.exec()  # Ejecuta el modal
        else:
            # Muestra un mensaje de advertencia si no se ha seleccionado un cliente
            MessageBox("Seleccione un cliente para ver los datos", "warning").show()

    def click_cliente(self, index: QModelIndex):
        """
        Maneja el evento de clic en una fila de la tabla de clientes, actualizando el cliente seleccionado.
        
        :param index: Índice de la fila clickeada en la tabla.
        """
        row = index.row()  # Obtiene la fila seleccionada
        cliente_id_item = self.model.item(row, 4)  # Obtiene el valor de la columna "Id" (oculta)

        # Si se encuentra un item en la columna "Id", actualiza el cliente seleccionado
        if cliente_id_item:
            self.cliente_seleccionado = cliente_id_item.text() or 0  # Actualiza el cliente seleccionado, si existe
