from PyQt6.QtWidgets import QMainWindow

from app.views.ui_ventana_crear_archivo import Ui_VentanaCrearArchivo


class VentanaCrearArchivo(QMainWindow, Ui_VentanaCrearArchivo):
    def __init__(self):
        super(VentanaCrearArchivo, self).__init__()
        self.setupUi(self)