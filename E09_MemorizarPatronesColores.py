import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
import random

qtCreatorFile = "E09_MemorizarPatronesColores.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)

        # Área de los Signals
        self.btn_iniciar.clicked.connect(self.iniciar)
        self.btn_reiniciar.clicked.connect(self.reiniciar)
        self.btn_1.clicked.connect(lambda: self.botonPresionado(self.btn_1))
        self.btn_2.clicked.connect(lambda: self.botonPresionado(self.btn_2))
        self.btn_3.clicked.connect(lambda: self.botonPresionado(self.btn_3))
        self.btn_4.clicked.connect(lambda: self.botonPresionado(self.btn_4))
        self.btn_5.clicked.connect(lambda: self.botonPresionado(self.btn_5))

        # Lista de colores
        self.lista_colores = [
            QtGui.QColor("blue"),
            QtGui.QColor("green"),
            QtGui.QColor("red"),
            QtGui.QColor("yellow"),
            QtGui.QColor("orange")
        ]

        # Lista de botones
        self.botones = [self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5]
        # Patrón correcto y selección del usuario
        self.patron_correcto = []
        self.seleccion_usuario = []
        # Estado del juego
        self.juego_iniciado = False

    # Área de los Slots
    def iniciar(self):
        if not self.juego_iniciado:
            self.btn_iniciar.setEnabled(False)
            self.patron_correcto = random.sample(self.lista_colores, len(self.lista_colores))
            self.mostrarPatron()
            self.juego_iniciado = True

    def mostrarPatron(self):
        for color, boton in zip(self.patron_correcto, self.botones):
            self.mostrarColorEnBoton(boton, color)
            QtCore.QCoreApplication.processEvents()  # Procesar los eventos para actualizar la interfaz
            QtCore.QThread.msleep(500)  # Esperar 500 milisegundos antes de mostrar el siguiente color

        self.limpiarColoresBotones()

    def mostrarColorEnBoton(self, boton, color):
        boton.setStyleSheet(f"background-color: {color.name()}; border: 1px solid black;")

    def botonPresionado(self, boton):
        if not self.juego_iniciado:
            return

        idx = self.botones.index(boton)
        color = self.lista_colores[idx]

        if color in self.seleccion_usuario:
            self.seleccion_usuario.remove(color)
            self.limpiarColorBoton(boton)
        else:
            self.seleccion_usuario.append(color)
            self.mostrarColorEnBoton(boton, color)

        if self.seleccion_usuario == self.patron_correcto[:len(self.seleccion_usuario)]:
            if len(self.seleccion_usuario) == len(self.patron_correcto):
                self.ganarJuego()
            else:
                QtWidgets.QMessageBox.information(self, "Correcto", f"Color {len(self.seleccion_usuario)} correcto.")
        else:
            QtWidgets.QMessageBox.information(self, "Incorrecto", "El color seleccionado no es correcto.")

    def limpiarColorBoton(self, boton):
        boton.setStyleSheet("")  # Restablece el estilo del botón

    def limpiarColoresBotones(self):
        for boton in self.botones:
            self.limpiarColorBoton(boton)

    def reiniciar(self):
        self.seleccion_usuario = []
        self.limpiarColoresBotones()
        self.juego_iniciado = False
        self.btn_iniciar.setEnabled(True)

    def ganarJuego(self):
        QtWidgets.QMessageBox.information(self, "¡Felicidades!", "¡Has ganado el juego!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
