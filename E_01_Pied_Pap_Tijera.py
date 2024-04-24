import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "E_01_Pied_Pap_Tijera.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_tijera.clicked.connect(self.elegir_tijera)
        self.btn_piedra.clicked.connect(self.elegir_piedra)
        self.btn_papel.clicked.connect(self.elegir_papel)
        self.btn_iniciar.clicked.connect(self.iniciar_juego)
        self.segundo = QtCore.QTimer()
        self.segundo.timeout.connect(self.carrusel)
        self.idx = 0

        self.lista_imagenes = [
            ":/Logos/piedra.jpeg",
            ":/Logos/papel.jpeg",
            ":/Logos/tijeras.jpeg",
        ]

        self.imagen_usuario = ":/Logos/piedra.jpeg"
        self.imagenPC.setPixmap(QtGui.QPixmap(self.lista_imagenes[0]))
        self.imagenUsu.setPixmap(QtGui.QPixmap(self.imagen_usuario))

    def iniciar_juego(self):
        t = self.btn_iniciar.text()
        if t == "INICIAR":
            self.btn_iniciar.setText("DETENER")
            self.idx = 0
            self.segundo.start(100)
            self.habilitar_botones_juego(True)
        else:
            self.btn_iniciar.setText("INICIAR")
            self.segundo.stop()
            self.habilitar_botones_juego(False)

    def habilitar_botones_juego(self, estado):
        self.btn_tijera.setEnabled(estado)
        self.btn_piedra.setEnabled(estado)
        self.btn_papel.setEnabled(estado)

    def carrusel(self):
        self.idx = (self.idx + 1) % len(self.lista_imagenes)
        self.imagenPC.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.idx]))

    def actualizar_imagen_usuario(self):
        self.imagenUsu.setPixmap(QtGui.QPixmap(self.imagen_usuario))

    def elegir_tijera(self):
        self.imagen_usuario = ":/Logos/tijeras.jpeg"
        self.actualizar_imagen_usuario()
        self.elegir_opcion("tijera")

    def elegir_piedra(self):
        self.imagen_usuario = ":/Logos/piedra.jpeg"
        self.actualizar_imagen_usuario()
        self.elegir_opcion("piedra")

    def elegir_papel(self):
        self.imagen_usuario = ":/Logos/papel.jpeg"
        self.actualizar_imagen_usuario()
        self.elegir_opcion("papel")

    def elegir_opcion(self, opcion):
        self.opcion_usuario = opcion
        self.segundo.stop()
        self.validar_resultado()

    def validar_resultado(self):
        opcion_pc = self.lista_imagenes[self.idx]

        if self.opcion_usuario == opcion_pc:
            resultado = "Empate"
        elif (
            (self.opcion_usuario == "tijera" and opcion_pc == ":/Logos/papel.jpeg") or
            (self.opcion_usuario == "papel" and opcion_pc == ":/Logos/piedra.jpeg") or
            (self.opcion_usuario == "piedra" and opcion_pc == ":/Logos/tijeras.jpeg")
        ):
            resultado = "Ganaste :)"
        elif (
            (self.opcion_usuario == "papel" and opcion_pc == ":/Logos/tijeras.jpeg") or
            (self.opcion_usuario == "piedra" and opcion_pc == ":/Logos/papel.jpeg") or
            (self.opcion_usuario == "tijera" and opcion_pc == ":/Logos/piedra.jpeg")
        ):
            resultado = "Perdiste :("
        else:
            resultado = "Empate"

        msj = QtWidgets.QMessageBox()
        msj.setText(resultado)
        msj.exec_()
        self.iniciar_juego()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
