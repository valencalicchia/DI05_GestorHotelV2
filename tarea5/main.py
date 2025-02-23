#!/usr/bin/python3
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog

from controladores.login_controller import LoginController
from controladores.bd_conn_controller import ConexionBDController
from controladores.main_controller import MainController

def login(app):
    """
    Función que maneja la ventana de login y retorna si el usuario ha iniciado sesión correctamente.

    Args:
        app (QApplication): Instancia de la aplicación Qt que se utilizará para ejecutar el ciclo de eventos de la GUI.

    Returns:
        bool: Retorna True si el login fue exitoso, False en caso contrario.
    """
    login_window = QMainWindow()
    login_controler = LoginController(login_window)
    login_window.show()

    # Inicia el ciclo de eventos de la aplicación Qt (esto hace que la ventana se muestre y se quede activa).
    app.exec()

    return login_controler.bLogado


def init_app(app):
    """
    Inicializa la aplicación principal después de un login exitoso.

    Esta función se encarga de crear la conexión a la base de datos y mostrar la ventana principal de la aplicación.

    Args:
        app (QApplication): Instancia de la aplicación Qt que se utilizará para ejecutar el ciclo de eventos de la GUI.
    """

    main_window = MainController()
    main_window.show()

    # Inicia el ciclo de eventos de la aplicación Qt, lo que permite que la ventana se mantenga abierta.
    app.exec()


def main():
    """
    Función principal que coordina el flujo de la aplicación.
    Inicia el proceso de login y, si es exitoso, inicializa la aplicación principal.
    """
    app = QApplication(sys.argv)

    style = """
QMainWindow {
    background-color: #f0f0f0;
    border-radius: 8px;
    padding: 20px;
}

QDialog {
    background-color: #f0f0f0;
    border-radius: 8px;
    padding: 20px;
}

QLabel {
    font-weight: bold;
    color: #333;
    margin-bottom: 10px;
}

QSpinBox {
    background-color: #ffffff;
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 12px;
    font-size: 16px;
    color: #333;
    min-width: 120px;  /* Asegura que tenga un tamaño adecuado */
    height: 40px;  /* Ajuste de altura para que no se corte el contenido */
}

QSpinBox:focus {
    border: 1px solid #4CAF50;
    background-color: #e8f5e9;
}

QSpinBox:disabled {
    background-color: #f0f0f0;
    color: #aaa;
    border: 1px solid #ddd;
}

QSpinBox::up-button, QSpinBox::down-button {
    background-color: #ffffff;
    border: 1px solid #ccc;
    width: 25px;
    height: 25px;
    border-radius: 4px;
    font-size: 16px;
    color: #333;
}

QSpinBox::up-button:hover, QSpinBox::down-button:hover {
    background-color: #e8f5e9;
}

QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {
    background-color: #4CAF50;
    color: white;
}

QSpinBox::up-button:disabled, QSpinBox::down-button:disabled {
    background-color: #f0f0f0;
    color: #aaa;
    border: 1px solid #ddd;
}

QLineEdit, QTextEdit, QComboBox, QDateEdit {
    background-color: #ffffff;
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 8px;
    font-size: 14px;
    color: #333;
}

QDateEdit {
    font-size: 14px;
}

QDateEdit::popup {
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #ffffff;
    font-size: 16px;
    padding: 10px;
}

QDateEdit QCalendarWidget {
    font-size: 16px;
    selection-background-color: #4CAF50; /* Color verde de selección */
    selection-color: white;
    border-radius: 8px;
}

QLineEdit:focus, QTextEdit:focus, QComboBox:focus:focus, QDateEdit:focus {
    border: 1px solid #4CAF50;
    background-color: #e8f5e9;
}

QLineEdit:disabled, QTextEdit:disabled, QComboBox:disabled:disabled, QDateEdit:disabled {
    background-color: #f0f0f0;
    color: #aaa;
    border: 1px solid #ddd;
}

QPushButton {
    background-color: #4CAF50;
    color: white;
    border: 1px solid #4CAF50;
    border-radius: 5px;
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #45a049;
}

QPushButton:pressed {
    background-color: #388e3c;
}

QPushButton:disabled {
    background-color: #ccc;
    color: #888;
    border: 1px solid #ccc;
}

QCheckBox {
    font-size: 14px;
    color: #333;
    padding-left: 10px;
    padding-right: 10px;
}

QCheckBox::indicator {
    width: 18px;
    height: 18px;
    border: 1px solid #ccc;
    border-radius: 3px;
    background-color: #ffffff;
}

QCheckBox::indicator:checked {
    background-color: #4CAF50;
    border: 1px solid #4CAF50;
}

QCheckBox::indicator:unchecked {
    background-color: #ffffff;
    border: 1px solid #ccc;
}

QCheckBox:disabled {
    color: #aaa;
}

QCheckBox:disabled::indicator {
    background-color: #f0f0f0;
    border: 1px solid #ddd;
}

QTableWidget, QTableView {
    background-color: #ffffff; /* Fondo blanco para la tabla */
    border: 1px solid #ccc;    /* Borde gris claro para la tabla */
    font-size: 14px;
    color: #333;
    border-radius: 4px;
    padding: 10px;
    gridline-color: #ccc; /* Color de las líneas de la cuadrícula */
}

QTableWidget::item, QTableView::item {
    padding: 15px;  /* Mayor padding para hacer las filas más gruesas */
    border-bottom: 1px solid #f0f0f0;  /* Separadores sutiles entre filas */
}

QTableWidget::item:selected, QTableView::item:selected {
    background-color: #4CAF50;  /* Fondo verde para las filas seleccionadas */
    color: white;
}

QTableWidget:disabled, QTableView:disabled {
    background-color: #f0f0f0;  /* Fondo gris para el estado deshabilitado */
    color: #aaa;                /* Color de texto gris claro */
}

QHeaderView::section {
    background-color: #4CAF50;  /* Fondo verde para los encabezados */
    color: white;
    padding: 10px;
    font-size: 16px;
    font-weight: bold;
    border: 1px solid #ccc;
    text-align: center;
    border-radius: 4px;
}

QHeaderView::section:hover {
    background-color: #45a049;  /* Cambio de fondo cuando se pasa el mouse */
}

QHeaderView::section:disabled {
    background-color: #f0f0f0;  /* Fondo gris para los encabezados deshabilitados */
    color: #aaa;
    border: 1px solid #ddd;
}


QMenu {
    background-color: #ffffff;
    border: 1px solid #ccc;
    font-size: 14px;
    color: #333;
}

QMenu::item {
    padding: 10px;
    border-bottom: 1px solid #f0f0f0;
}

QMenu::item:selected {
    background-color: #4CAF50;
    color: white;
}

QMenu::item:disabled {
    background-color: #f0f0f0;
    color: #aaa;
}

QMenuBar {
    background-color: #4CAF50;
    color: white;
    font-size: 16px;
    font-weight: bold;
}

QMenuBar::item {
    padding: 10px;
}

QMenuBar::item:selected {
    background-color: #45a049;
}

QMenuBar::item:disabled {
    background-color: #ccc;
    color: #888;
}

QComboBox:disabled {
    background-color: #f0f0f0;
    color: #aaa;
    border: 1px solid #ddd;
}

QListWidget {
    background-color: #ffffff;
    border: 1px solid #ccc;
    font-size: 14px;
    color: #333;
}

QListWidget::item {
    padding: 8px;
    border-bottom: 1px solid #f0f0f0;
}

QListWidget::item:selected {
    background-color: #4CAF50;
    color: white;
}

QListWidget:disabled {
    background-color: #f0f0f0;
    color: #aaa;
}

QTableView {
    background-color: #ffffff;
    border: 1px solid #ccc;
    font-size: 14px;
    color: #333;
}

QTableView::item {
    padding: 8px;
    border-bottom: 1px solid #f0f0f0;
}

QTableView::item:selected {
    background-color: #4CAF50;
    color: white;
}

QTableView:disabled {
    background-color: #f0f0f0;
    color: #aaa;
}


"""
    
    # Añade los estilos para toda la app
    app.setStyleSheet(style)

    config_window = ConexionBDController()
    config_window.setModal(True)

    if config_window.exec() == QDialog.Accepted:
        if login(app):
            init_app(app)


# Bloque que asegura que el código se ejecute solo si el script es ejecutado directamente.
if __name__ == "__main__":
    main()
