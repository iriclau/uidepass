import sys

from PyQt6.QtWidgets import QApplication

from app.views.ventana_principal import VentanaPrincipal


def main():
    app=QApplication(sys.argv)
    ventana_principal=VentanaPrincipal()
    ventana_principal.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()