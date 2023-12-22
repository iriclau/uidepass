from PyQt6.QtWidgets import QMainWindow

from app.functions.password import generar_contrasena_randomica
from app.views.qt.ui_ventana_nueva_contrasena import Ui_VentanaNuevaContrasena


class VentanaNuevaContrasena(QMainWindow, Ui_VentanaNuevaContrasena):

    def __init__(self, ruta_archivo, ventana_lista_contrasena):
        super(VentanaNuevaContrasena, self).__init__()

        self.ventana_lista_contrasena = ventana_lista_contrasena
        self.ruta_archivo = ruta_archivo

        self.setupUi(self)
        self.btn_generar.clicked.connect(self.generar_contrasena)
        self.btn_cancelar.clicked.connect(self.cancelar)

    def cancelar(self):
        self.close()

    def generar_contrasena(self):
        cuenta = self.input_cuenta.text()
        detalle = self.input_detalle.text()
        contrasena = generar_contrasena_randomica(15)

        with open(self.ruta_archivo, "a") as archivo:
            archivo.write(cuenta + ";" + detalle + ";" + contrasena + "\n")

        archivo.close()
        self.ventana_lista_contrasena.llena_tabla()
        self.close()
