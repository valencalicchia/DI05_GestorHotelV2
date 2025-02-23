from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QDate
import re

from vistas.create_edit_cliente_ui import Ui_Cliente

from modelos.datos import ClientesDAO, ReservasDAO
from modelos.models import ClienteModel

from utilidades.message_box import MessageBox


class ClienteController(QDialog):
    """
    Controlador para la ventana de gestión de clientes, que permite la creación, 
    modificación y eliminación de un cliente.
    """
    def __init__(self, cliente_id):
        """
        Constructor de la clase ClienteController.

        Parámetros:
        cliente_id (int): ID del cliente a editar. Si es 0, se crea un nuevo cliente.
        """
        try:
            super().__init__()  # Inicializa el QDialog
            self.ui = Ui_Cliente()  # Instancia de la interfaz de usuario
            self.ui.setupUi(self)  # Configura la UI

            self.init_daos()  # Inicializa los DAOs necesarios
            self.config_events()  # Configura los eventos de los botones

            if cliente_id:  # Si se pasa un ID de cliente, se edita ese cliente
                self.cliente_id = cliente_id
                self.cliente_modificacion = self.dao_clientes.get(self.cliente_id)  # Obtiene los datos del cliente
                self.es_nueva = False  # No es un cliente nuevo
                self.en_edicion = False  # El cliente no está en edición
                
            else:  # Si no se pasa un ID, es un nuevo cliente
                self.cliente_id = 0
                self.es_nueva = True  # Es un cliente nuevo
                self.en_edicion = True  # Está en edición
                self.cliente_modificacion = ClienteModel("","","","","","","","","","")  # Datos vacíos para el nuevo cliente
                self.ui.vcbtnEliminar.setVisible(False)  # Oculta el botón de eliminar para el nuevo cliente

            self.cambiar_modo()  # Cambia el modo de la interfaz (edición o visualización)
            self.init_ui()  # Inicializa los elementos de la interfaz

        except Exception as e:
            # Si ocurre un error al cargar el formulario, muestra un mensaje de error
            MessageBox("Error al cargar el formulario de clientes", "error", str(e)).show()

    def config_events(self):
        """
        Configura los eventos de los botones de la interfaz.

        Enlaza los botones de confirmar y eliminar con sus respectivos métodos.
        """
        self.ui.vcbtnConfirmar.clicked.connect(self.accion_btn_clientes)
        self.ui.vcbtnEliminar.clicked.connect(self.accion_btn_eliminar)

    def accion_btn_clientes(self):
        """
        Lógica para el botón de confirmar. Permite cambiar entre los modos de edición 
        y visualización del cliente.
        """
        if self.en_edicion:  # Si está en modo edición
            if self.confirm_cliente():  # Confirma los datos del cliente
                self.en_edicion = not self.en_edicion  # Cambia el estado de edición
                self.cambiar_modo()  # Cambia el modo de la interfaz
        else:  # Si no está en edición
            self.en_edicion = not self.en_edicion  # Cambia el estado de edición
            self.cambiar_modo()  # Cambia el modo de la interfaz
        
    def accion_btn_eliminar(self):
        """
        Lógica para el botón de eliminar. Si está en edición, cancela los cambios. 
        Si no está en edición, elimina al cliente.
        """
        if self.en_edicion:
            self.en_edicion = False  # Sale del modo de edición
            self.cambiar_modo()  # Cambia el modo
            self.rellenar_datos()  # Rellena los datos del cliente
        else:
            self.eliminar_cliente()  # Elimina al cliente

    def cambiar_modo(self):
        """
        Cambia entre el modo de edición y visualización de la interfaz de usuario.
        """
        if not self.en_edicion:  # Si no está en edición
            self.ui.vcbtnConfirmar.setText("Editar")    
            self.ui.vcbtnEliminar.setText("Eliminar")    
        else:  # Si está en edición
            self.ui.vcbtnConfirmar.setText("Confirmar")    
            self.ui.vcbtnEliminar.setText("Cancelar")    

        # Habilita o deshabilita los campos según el estado de edición
        self.ui.vcchkBoxMenores.setEnabled(self.en_edicion)
        self.ui.vccboBoxSexo.setEnabled(self.en_edicion)
        self.ui.vcdateEdit.setEnabled(self.en_edicion)
        self.ui.vcTxtApellidos.setEnabled(self.en_edicion)
        self.ui.vcTxtDni.setEnabled(self.en_edicion)
        self.ui.vcTxtEmail.setEnabled(self.en_edicion)
        self.ui.vcTxtNombre.setEnabled(self.en_edicion)
        self.ui.vcTxtPais.setEnabled(self.en_edicion)
        self.ui.vcTxtTelefono.setEnabled(self.en_edicion)

    def eliminar_cliente(self):
        """
        Elimina al cliente de la base de datos después de confirmar la acción.
        """
        respuesta = MessageBox("¿Desea eliminar este cliente? Esto eliminará también todas las reservas a su nombre", "question", buttons=("Yes", "No")).show()
        if respuesta == "Yes":
            # Elimina las reservas y al cliente
            self.dao_reserva.delete_by_cliente(self.cliente_id)
            self.dao_clientes.delete(self.cliente_id)

            respuesta = MessageBox("Cliente eliminado").show()  # Muestra mensaje de éxito
            if respuesta:
                self.accept()  # Cierra la ventana de cliente
                self.close()

    def validar_dni_nie_nif(self, nif):
        """
        Valida el formato y la corrección de un DNI, NIE o NIF.

        Parámetros:
        nif (str): Número de identificación a validar.

        Retorna:
        bool: True si el formato es válido, False si no lo es.
        """
        nif = nif.upper().strip()  # Convierte a mayúsculas y elimina espacios

        # Valida el DNI
        if re.match(r'^\d{8}[A-Z]$', nif):
            dni = nif[:8]
            letra = nif[-1]
            letras_validas = "TRWAGMYFPDXBNJZSQVHLCKE"  # Letras válidas para la comprobación
            letra_correcta = letras_validas[int(dni) % 23]  # Calcula la letra correcta
            if letra == letra_correcta:
                return True
            else:
                return False

        # Valida el NIE
        elif re.match(r'^[XYZ]\d{7}[A-Z]$', nif):
            letra_inicial = nif[0]
            if letra_inicial == 'X':
                dni = '0' + nif[1:8]
            elif letra_inicial == 'Y':
                dni = '1' + nif[1:8]
            else:  # 'Z'
                dni = '2' + nif[1:8]
            
            letra = nif[-1]
            letras_validas = "TRWAGMYFPDXBNJZSQVHLCKE"
            letra_correcta = letras_validas[int(dni) % 23]
            if letra == letra_correcta:
                return True
            else:
                return False

        # Valida otro tipo de identificación
        elif re.match(r'^\d{8}[A-HJ-NP-TV-Z]$', nif):
            return True
        
        return False

    def init_ui(self):
        """
        Inicializa los elementos de la interfaz, añadiendo los valores predeterminados.
        """
        try:
            self.ui.vccboBoxSexo.addItem('M')
            self.ui.vccboBoxSexo.addItem('H')

            self.set_fecha()  # Establece la fecha de nacimiento

            if not self.es_nueva:  # Si no es un cliente nuevo, rellena los datos
                self.rellenar_datos() 

        except Exception as e:
            MessageBox("Error al inicializar la UI", "error", str(e)).show()

    def init_daos(self):
        """
        Inicializa los DAOs necesarios para interactuar con la base de datos.
        """
        try:
            self.dao_reserva = ReservasDAO()  # DAO para reservas
            self.dao_clientes = ClientesDAO()  # DAO para clientes

        except Exception as e:
            MessageBox("Error al inicializar los DAOS", "error", str(e)).show()

    def rellenar_datos(self):
        """
        Rellena los campos de la interfaz con los datos del cliente a modificar.
        """
        self.ui.vccboBoxSexo.setCurrentText(self.cliente_modificacion.sexo)
        self.ui.vcTxtTelefono.setText(self.cliente_modificacion.telefono)
        self.ui.vcTxtNombre.setText(self.cliente_modificacion.nombre)
        self.ui.vcTxtApellidos.setText(self.cliente_modificacion.apellidos)
        self.ui.vcTxtDni.setText(self.cliente_modificacion.num_identificacion)
        self.ui.vcTxtPais.setText(self.cliente_modificacion.pais)
        self.ui.vcTxtEmail.setText(self.cliente_modificacion.email)
        self.ui.vcchkBoxMenores.setChecked(self.cliente_modificacion.menores == 1)

    def set_fecha(self):
        """
        Establece la fecha de nacimiento del cliente en el campo correspondiente.
        """
        fecha_hoy = QDate.currentDate()  # Fecha actual
        if not self.es_nueva:
            fecha_str = self.cliente_modificacion.fec_nac.strftime("%Y-%m-%d")
            fecha = QDate.fromString(fecha_str, "yyyy-MM-dd")
        else:
            fecha = fecha_hoy

        self.ui.vcdateEdit.setDate(fecha)  # Establece la fecha en el campo
        self.ui.vcdateEdit.setMaximumDate(fecha_hoy)  # La fecha máxima es la fecha de hoy
        self.ui.vcdateEdit.setCalendarPopup(True)
        self.ui.vcdateEdit.setDisplayFormat("yyyy-MM-dd")

    def confirm_cliente(self):
        """
        Confirma si los datos del cliente son válidos antes de proceder con la operación.

        Retorna:
        bool: True si los datos son válidos, False si no lo son.
        """
        dni = self.ui.vcTxtDni.text().strip()
        nombre = self.ui.vcTxtNombre.text().strip()
        apellidos = self.ui.vcTxtApellidos.text().strip()

        # Verifica si los campos obligatorios están vacíos
        if not bool(nombre) or not bool(apellidos) or not bool(dni):
            MessageBox("Todos los campos 'Nombre', 'Apellidos', 'DNI' son obligatorios.", "warning").show()
            return False
        
        # Valida el formato del DNI
        if not self.validar_dni_nie_nif(dni):
            MessageBox("Por favor, introduzca un DNI/NIE/NIF válido", "warning").show()
            return False
        
        # Si todo es válido, crea un objeto cliente
        cliente = self.set_cliente(dni, nombre, apellidos)
        if cliente:
            self.safe(cliente)  # Guarda los cambios
            return True

    def set_cliente(self, dni, nombre, apellidos):
        """
        Crea un objeto cliente con los datos proporcionados si el DNI no está duplicado.

        Parámetros:
        dni (str): DNI del cliente
        nombre (str): Nombre del cliente
        apellidos (str): Apellidos del cliente

        Retorna:
        ClienteModel: Un objeto cliente con los datos proporcionados si el DNI es válido, 
        None si el DNI ya existe.
        """
        if self.dao_clientes.checkDniExiste(dni, self.cliente_id) == False:
            return ClienteModel(
                id=self.cliente_id,
                nombre=nombre,
                apellidos=apellidos,
                num_identificacion=dni,
                fec_nac=self.ui.vcdateEdit.date().toPython(),
                pais=self.ui.vcTxtPais.text().strip(),
                telefono=self.ui.vcTxtTelefono.text().strip(),
                email=self.ui.vcTxtNombre.text().strip(),
                sexo=self.ui.vccboBoxSexo.currentData(),
                menores=int(self.ui.vcchkBoxMenores.isChecked())
            )
        else:
            MessageBox("Ya hay un cliente con el mismo DNI", "warning").show()

        return None

    def safe(self, cliente):
        """
        Guarda los datos del cliente en la base de datos (crea o actualiza).

        Parámetros:
        cliente (ClienteModel): El objeto cliente con los datos a guardar.
        """
        try:
            if not self.es_nueva:  # Si no es un cliente nuevo, actualiza el cliente
                self.dao_clientes.update(cliente)
            else:  # Si es un cliente nuevo, crea uno nuevo en la base de datos
                self.dao_clientes.create(cliente)

            respuesta = MessageBox("Operación exitosa").show()  # Muestra un mensaje de éxito
            if respuesta:
                self.accept()  # Acepta la operación
                self.close()  # Cierra el formulario

        except Exception as e:
            # Si ocurre un error al guardar, muestra un mensaje de error
            MessageBox("Error al procesar la operación", "error", str(e)).show()
