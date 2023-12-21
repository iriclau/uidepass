from PyQt6.QtWidgets import QMainWindow

from app.views.qt.ui_ventana_nueva_contrasena import Ui_VentanaNuevaContrasena


class VentanaNuevaContrasena(QMainWindow, Ui_VentanaNuevaContrasena):
    def __init__(self):
        super(VentanaNuevaContrasena, self).__init__()
        self.setupUi(self)