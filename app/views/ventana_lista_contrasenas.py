from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QMainWindow

from app.views.qt.ui_ventana_lista_contrasenas import Ui_VentanaListaContrasenas
from app.views.ventana_nueva_contrasena import VentanaNuevaContrasena


class VentanaListaContrasenas(QMainWindow, Ui_VentanaListaContrasenas):

    def __init__(self, ruta_archivo):
        super(VentanaListaContrasenas, self).__init__()
        self.setupUi(self)

        self.ruta_archivo = ruta_archivo

        self.lista_contrasenas = []
        self.llena_tabla()
        self.btn_crear_nueva.clicked.connect(self.abrir_pantalla_nueva_contrasena)
        self.btn_cerrar_sesion.clicked.connect(self.cerrar_sesion)

    def cerrar_sesion(self):
        self.close()
    def abrir_pantalla_nueva_contrasena(self):
        self.ventana_nueva_contrasena = VentanaNuevaContrasena(self.ruta_archivo, self)
        self.ventana_nueva_contrasena.show()

    def llena_tabla(self):
        self.lista_contrasenas = []
        with open(self.ruta_archivo, "r") as archivo:
            for linea in archivo:
                cuenta, detalle, contrasena = linea.strip().split(";")
                self.lista_contrasenas.append((cuenta, detalle, contrasena))

        modelo = QStandardItemModel(len(self.lista_contrasenas), 3)
        modelo.setHorizontalHeaderLabels(["Cuenta", "Detalle", "Contraseña"])
        for fila, (cuenta, detalle, contrasena) in enumerate(self.lista_contrasenas):
            item_cuenta = QStandardItem(cuenta)
            item_detalle = QStandardItem(detalle)
            item_contrasena = QStandardItem(contrasena)
            modelo.setItem(fila, 0, item_cuenta)
            modelo.setItem(fila, 1, item_detalle)
            modelo.setItem(fila, 2, item_contrasena)
        self.table_lista_contrasenas.setModel(modelo)
