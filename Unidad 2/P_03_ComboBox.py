import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P_03_ComboBox.ui"  # Nombre del archivo aquí.
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

        self.combo_equipo.addItem("Selecciona...", 0)
        self.combo_equipo.addItem("Raul", 1)
        self.combo_equipo.addItem("Bonilla", 2)
        self.combo_equipo.addItem("Amando", 3)
        self.combo_equipo.addItem("Jeremy", 4)
        self.combo_equipo.addItem("Frida", 5)

        self.combo_equipo.currentIndexChanged.connect(self.cambia)

    def cambia(self):
        print("Text: " + self.combo_equipo.currentText())
        print("Index: " + str(self.combo_equipo.currentIndex()))
        print("Data: " + str(self.combo_equipo.currentData()))

        dataClave = self.combo_equipo.currentData()
        imagen = self.datos_alumno[dataClave][-1]
        self.img_persona.setPixmap(QtGui.QPixmap(imagen))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

