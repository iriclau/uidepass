# Form implementation generated from reading ui file '.\app\views\qt\design\ventana_nueva_contrasena.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_VentanaNuevaContrasena(object):
    def setupUi(self, VentanaNuevaContrasena):
        VentanaNuevaContrasena.setObjectName("VentanaNuevaContrasena")
        VentanaNuevaContrasena.resize(554, 467)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=VentanaNuevaContrasena)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 60, 311, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.input_cuenta = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.input_cuenta.setObjectName("input_cuenta")
        self.verticalLayout.addWidget(self.input_cuenta)
        self.input_detalle = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.input_detalle.setObjectName("input_detalle")
        self.verticalLayout.addWidget(self.input_detalle)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=VentanaNuevaContrasena)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 300, 401, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_cancelar = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.horizontalLayout.addWidget(self.btn_cancelar)
        self.btn_generar = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_generar.setObjectName("btn_generar")
        self.horizontalLayout.addWidget(self.btn_generar)
        self.label = QtWidgets.QLabel(parent=VentanaNuevaContrasena)
        self.label.setGeometry(QtCore.QRect(40, 90, 231, 20))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=VentanaNuevaContrasena)
        self.label_3.setGeometry(QtCore.QRect(100, 140, 111, 20))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(VentanaNuevaContrasena)
        QtCore.QMetaObject.connectSlotsByName(VentanaNuevaContrasena)

    def retranslateUi(self, VentanaNuevaContrasena):
        _translate = QtCore.QCoreApplication.translate
        VentanaNuevaContrasena.setWindowTitle(_translate("VentanaNuevaContrasena", "Dialog"))
        self.btn_cancelar.setText(_translate("VentanaNuevaContrasena", "Cancelar"))
        self.btn_generar.setText(_translate("VentanaNuevaContrasena", "Generar"))
        self.label.setToolTip(_translate("VentanaNuevaContrasena", "Ejemplo, (Facebook)"))
        self.label.setText(_translate("VentanaNuevaContrasena", "Ingresa nombre de la cuenta:"))
        self.label_3.setToolTip(_translate("VentanaNuevaContrasena", "Ejemplo cuenta de facebook juanitoperez@gmail.com"))
        self.label_3.setText(_translate("VentanaNuevaContrasena", "Ingresa el detalle:"))