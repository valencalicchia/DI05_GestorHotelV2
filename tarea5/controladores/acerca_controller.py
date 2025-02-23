from PySide6.QtWidgets import QDialog

from vistas.ui_acerca_de import Ui_Acerca

class AcercaController(QDialog):
    '''
    Clase que se encarga de mostrar el apartado de "Acerca de"
    '''
    def __init__(self):
        super().__init__()
        self.ui = Ui_Acerca()  
        self.ui.setupUi(self)  