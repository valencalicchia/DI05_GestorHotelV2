from PySide6.QtWidgets import QMainWindow

from vistas.menu_principal_ui import Ui_MenuPrincipal

from controladores.docu_controller import DocuController
from controladores.acerca_controller import AcercaController
from controladores.clientes_controller import ClientesController
from controladores.reservas_controller import ReservasController

from controladores.docu_controller import DocuController
from utilidades.message_box import MessageBox

class MainController(QMainWindow):
    def __init__(self):

        super().__init__()
        self.ui = Ui_MenuPrincipal() 
        self.ui.setupUi(self)  

        self.init_ui() 

    def init_ui(self):
        try:
            self.ui.actionDocumentaci_n.triggered.connect(lambda: self.show_controller(DocuController))
            self.ui.actionAcerca.triggered.connect(lambda: self.show_controller(AcercaController))
            self.ui.actionClientes.triggered.connect(lambda: self.show_controller(ClientesController))
            self.ui.actionReservar.triggered.connect(lambda: self.show_controller(ReservasController))

        except Exception as e:
            MessageBox("Error al configurar la UI", "error", str(e)).show()

    def show_controller(self, Controller):
        try:
            controller = Controller()
            controller.setModal(True)
            controller.exec()

        except Exception as e:
            MessageBox("Error al configurar la UI", "error", str(e)).show()

