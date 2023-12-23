from PyQt6.QtWidgets import QMainWindow, QFileDialog

from app.views.qt.ui_ventana_crear_archivo import Ui_VentanaCrearArchivo
from app.views.ventana_lista_contrasenas import VentanaListaContrasenas


class VentanaCrearArchivo(QMainWindow, Ui_VentanaCrearArchivo):
    def __init__(self):
        super(VentanaCrearArchivo, self).__init__()
        self.setupUi(self)
        self.path_carpeta = ""
        self.ruta_archivo = ""

        self.btn_crear_archivo.clicked.connect(self.crear_archivo)
        self.btn_seleccionar_donde_guardar.clicked.connect(self.seleccionar_donde_guardar)
        self.btn_cancelar.clicked.connect(self.cerrar)

    def cerrar(self):
        self.close()

    def seleccionar_donde_guardar(self):
        path_carpeta = QFileDialog.getExistingDirectory(self, "seleccionar una carpeta")
        if path_carpeta:
            self.path_carpeta = path_carpeta
            self.label_ruta_carpeta.setText(path_carpeta)

    def crear_archivo(self):
        nombre_archivo = self.input_nombre_archivo.text()
        nombre_archivo_mas_extension = nombre_archivo + ".uidepass"

        self.ruta_archivo = self.path_carpeta + "/" + nombre_archivo_mas_extension

        with open(self.ruta_archivo, "w") as archivo:
            pass
        archivo.close()

        self.ventana_lista_contrasenas = VentanaListaContrasenas(self.ruta_archivo)

        self.ventana_lista_contrasenas.show()
        self.close()
