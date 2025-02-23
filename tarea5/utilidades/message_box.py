from PySide6.QtWidgets import QMessageBox

class MessageBox(QMessageBox):
    def __init__(self, message, message_type="info", details=None, buttons=("Ok",)):
        """
        Inicializa un cuadro de mensaje genérico.

        Args:
            message (str): El mensaje a mostrar.
            message_type (str): Tipo de mensaje ('info', 'error', 'warning', 'success', 'question').
            details (str, opcional): Detalles adicionales del mensaje.
            buttons (tuple, opcional): Botones a mostrar ('Ok', 'Cancel', 'Yes', 'No', etc.).
        """
        super().__init__()
        self.setWindowTitle(message_type.capitalize())
        self.setText(message)

        icon_mapping = {
            "info": QMessageBox.Icon.Information,
            "error": QMessageBox.Icon.Critical,
            "warning": QMessageBox.Icon.Warning,
            "success": QMessageBox.Icon.Information,
            "question": QMessageBox.Icon.Question,
        }
        self.setIcon(icon_mapping.get(message_type, QMessageBox.Icon.Information))

        if details:
            self.setDetailedText(details)

        button_mapping = {
            "Ok": QMessageBox.StandardButton.Ok,
            "Cancel": QMessageBox.StandardButton.Cancel,
            "Yes": QMessageBox.StandardButton.Yes,
            "No": QMessageBox.StandardButton.No,
            "Retry": QMessageBox.StandardButton.Retry,
            "Ignore": QMessageBox.StandardButton.Ignore,
            "Close": QMessageBox.StandardButton.Close,
        }

        # Aplicar los botones seleccionados con la operación de combinación de bits (|)
        selected_buttons = QMessageBox.StandardButton.NoButton
        for b in buttons:
            if b in button_mapping:
                selected_buttons |= button_mapping[b]

        self.setStandardButtons(selected_buttons)
        # Estilo para aumentar el tamaño de la fuente de los mensajes.
        self.setStyleSheet("""
            QLabel {
                font-size: 16px;  /* Tamaño de fuente de 14px para el mensaje */
                color: #333;  /* Color del texto */
            }
            QTextEdit {
                font-size: 16px;  /* Tamaño de fuente de 14px para el texto detallado */
                color: #333;  /* Color del texto */
            }
        """)

    def show(self):
        """
        Muestra el cuadro de mensaje y devuelve el botón seleccionado.

        Returns:
            str: El botón que el usuario seleccionó.
        """
        response = self.exec()
        for name, btn in QMessageBox.StandardButton.__members__.items():
            if btn == response:
                return name  # Devuelve el nombre del botón seleccionado
