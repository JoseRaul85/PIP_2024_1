import sys
from PyQt5 import uic, QtWidgets, QtCore
import pygame
from datetime import datetime

qtCreatorFile = "E_02_Alarma.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_iniciar.clicked.connect(self.iniciar)
        self.btn_cancelar.clicked.connect(self.cancelar)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.checar)
        self.sonando = False
        pygame.mixer.init()

    def iniciar(self):
        alarma = self.timeEdit_alarma.time()
        self.tiempo_alarma = alarma.toString("hh:mm")
        self.timer.start(1000)

        # Mostrar mensaje con la hora de alarma establecida
        hora_actual = datetime.now().strftime("%H:%M")
        cadena = f"Alarma establecida a las {self.tiempo_alarma} (Hora actual: {hora_actual})"
        msj = QtWidgets.QMessageBox()
        msj.setText(cadena)
        msj.exec_()

    def checar(self):
        tiempo = QtCore.QTime.currentTime()
        alarma = self.timeEdit_alarma.time()
        if tiempo.hour() == alarma.hour() and tiempo.minute() == alarma.minute() and not self.sonando:
            cadena = "¡Despierta!"
            msj = QtWidgets.QMessageBox()
            msj.setText(cadena)
            msj.addButton('Alarma', QtWidgets.QMessageBox.RejectRole)
            msj.exec_()
            pygame.mixer.music.load("the-synthwave-138196.wav")
            pygame.mixer.music.play()
            self.sonando = True

    def cancelar(self):
        self.timer.stop()
        pygame.mixer.music.stop()
        self.sonando = False
        QtWidgets.QMessageBox.information(self, "Alarma Cancelada", "La alarma ha sido cancelada.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
