import hashlib

from PyQt6.QtWidgets import QMainWindow, QFileDialog

from app.views.qt.ui_ventana_principal import Ui_VentanaPrincipal
from app.views.ventana_crear_archivo import VentanaCrearArchivo
from app.views.ventana_lista_contrasenas import VentanaListaContrasenas


class VentanaPrincipal(QMainWindow, Ui_VentanaPrincipal):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.setupUi(self)

        self.ruta_archivo = ""

        self.btn_seleccionar_archivo.clicked.connect(self.seleccionar_archivo)
        self.btn_crear_archivo.clicked.connect(self.crear_archivo)
        self.btn_ver_contrasenas.clicked.connect(self.ver_lista_contrasenas)

    def crear_archivo(self):
        self.ventana_crear_archivo = VentanaCrearArchivo()
        self.ventana_crear_archivo.show()

    def seleccionar_archivo(self):
        ruta_archivo, _ =QFileDialog.getOpenFileName(self, "seleccionar archivo", "", "archivos uidepass (*.uidepass)")
        if ruta_archivo:
            self.ruta_archivo = ruta_archivo

    def ver_lista_contrasenas(self):
        self.ventana_lista_contrasenas = VentanaListaContrasenas(self.ruta_archivo)

        self.ventana_lista_contrasenas.show()