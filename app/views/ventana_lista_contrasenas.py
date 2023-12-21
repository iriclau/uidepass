from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QMainWindow

from app.views.qt.ui_ventana_lista_contrasenas import Ui_VentanaListaContrasenas
from app.views.ventana_nueva_contrasena import VentanaNuevaContrasena


class VentanaListaContrasenas(QMainWindow, Ui_VentanaListaContrasenas):

    def __init__(self):
        super(VentanaListaContrasenas, self).__init__()
        self.setupUi(self)
        self.lista_contrasenas= [("Cuenta1", "Detalle1", "Contraseña1"),("Cuenta2", "Detalle2", "Contraseña2")]
        self.llena_tabla()
        self.btn_crear_nueva.clicked.connect(self.abrir_pantalla_nueva_contrasena)

    def abrir_pantalla_nueva_contrasena(self):
        self.ventana_nueva_contrasena = VentanaNuevaContrasena()
        self.ventana_nueva_contrasena.show()
    def llena_tabla(self):
        modelo = QStandardItemModel(len(self.lista_contrasenas),3)
        modelo.setHorizontalHeaderLabels(["Cuenta", "Detalle", "Contraseña"])
        for fila, (cuenta,detalle,contrasena) in enumerate(self.lista_contrasenas):
            item_cuenta = QStandardItem(cuenta)
            item_detalle = QStandardItem(detalle)
            item_contrasena = QStandardItem(contrasena)
            modelo.setItem(fila,0,item_cuenta)
            modelo.setItem(fila,1,item_detalle)
            modelo.setItem(fila,2,item_contrasena)
        self.table_lista_contrasenas.setModel(modelo)