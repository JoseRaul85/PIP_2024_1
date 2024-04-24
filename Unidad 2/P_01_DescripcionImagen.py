import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P_01_DescripcionImagen.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.datos_alumno = {
            1: ["Raul", "Futbol", 20, "RHO Positivo", ":/Logos/yo xd.jpg"],
            2: ["Bonilla", "Futbol", 20, "O Positivo", ":/Logos/bonillas.jpeg"],
            3: ["Amando", "Videojuegos", 20, "IT Negativo", ":/Logos/amando xd.jpeg"],
            4: ["Jeremy", "Gimnasio", 20, "SAT Positivo", ":/Logos/jeremias.jpeg"],
            5: ["Frida", "Compras", 20, "URS Positivo", ":/Logos/foto.jpeg"]
        }

        self.btn_atras.clicked.connect(self.atras)
        self.btn_adelante.clicked.connect(self.adelante)
        self.index_control = 0
        self.btn_atras.setEnabled(False)

    def atras(self):
        if self.index_control > 1:
            self.index_control -= 1
            datos = self.datos_alumno[self.index_control]
            print(datos)
            self.btn_adelante.setEnabled(True)
            self.img_persona.setPixmap(QtGui.QPixmap(datos[-1]))
        if self.index_control == 1:
            self.btn_atras.setEnabled(False)

    def adelante(self):
        if self.index_control < 5:
            self.index_control += 1
            datos = self.datos_alumno[self.index_control]
            print(datos)
            self.btn_atras.setEnabled(True)
            self.img_persona.setPixmap(QtGui.QPixmap(datos[-1]))
        if self.index_control == 5:
            self.btn_adelante.setEnabled(False)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

