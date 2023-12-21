from PyQt6.QtWidgets import QMainWindow

from app.views.qt.ui_ventana_crear_archivo import Ui_VentanaCrearArchivo


class VentanaCrearArchivo(QMainWindow, Ui_VentanaCrearArchivo):
    def __init__(self):
        super(VentanaCrearArchivo, self).__init__()
        self.setupUi(self)
        self.btn_crear_archivo.clicked.connect(self.crear_archivo)

    def crear_archivo(self):
        pass