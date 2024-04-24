import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "P_13_SeleccionEquipo.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.rb_amando.clicked.connect(self.clic_amando)
        self.rb_bonilla.clicked.connect(self.clic_bonilla)
        self.rb_jeremy.clicked.connect(self.clic_jeremy)
        self.rb_raul.clicked.connect(self.clic_raul)
        self.rb_frida.clicked.connect(self.clic_frida)
        self.rb_amando.toggled.connect(self.toggle_amando)
        self.rb_bonilla.toggled.connect(self.toggle_bonilla)
        self.rb_jeremy.toggled.connect(self.toggle_jeremy)
        self.rb_raul.toggled.connect(self.toggle_raul)
        self.rb_frida.toggled.connect(self.toggle_frida)

    def clic_amando(self):
        self.actualizar_equipo("Amando")

    def clic_bonilla(self):
        self.actualizar_equipo("Bonilla")

    def clic_jeremy(self):
        self.actualizar_equipo("Jeremy")

    def clic_raul(self):
        self.actualizar_equipo("Raúl")

    def clic_frida(self):
        self.actualizar_equipo("Frida")

    def toggle_amando(self):
        estado = self.rb_amando.isChecked()
        print(f"Amando cambió de estado (toggle). Nuevo Estado: {estado}")

    def toggle_bonilla(self):
        estado = self.rb_bonilla.isChecked()
        print(f"Bonilla cambió de estado (toggle). Nuevo Estado: {estado}")

    def toggle_jeremy(self):
        estado = self.rb_jeremy.isChecked()
        print(f"Jeremy cambió de estado (toggle). Nuevo Estado: {estado}")

    def toggle_raul(self):
        estado = self.rb_raul.isChecked()
        print(f"Raúl cambió de estado (toggle). Nuevo Estado: {estado}")

    def toggle_frida(self):
        estado = self.rb_frida.isChecked()
        print(f"Frida cambió de estado (toggle). Nuevo Estado: {estado}")

    def actualizar_equipo(self, nombre):
        self.txt_equipo.setText(nombre)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
