from PyQt6.QtWidgets import QMainWindow, QFileDialog

from app.views.ui_ventana_principal import Ui_VentanaPrincipal
from app.views.ventana_crear_archivo import VentanaCrearArchivo


class VentanaPrincipal(QMainWindow, Ui_VentanaPrincipal):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.setupUi(self)
        self.btn_seleccionar_archivo.clicked.connect(self.seleccionar_archivo)
        self.btn_crear_archivo.clicked.connect(self.crear_archivo)

    def crear_archivo(self):
        self.ventana_crear_archivo= VentanaCrearArchivo()
        self.ventana_crear_archivo.show()

    def seleccionar_archivo(self):
        ruta_archivo, _ =QFileDialog.getOpenFileName(self, "seleccionar archivo", "", "archivos uidepass (*.uidepass)")
        if ruta_archivo:
            print(ruta_archivo)