import sys
from PyQt5 import uic, QtWidgets, QtCore
import pygame

qtCreatorFile = "E_02_AlarmaV2.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_iniciar.clicked.connect(self.iniciar)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.checar)
        pygame.mixer.init()

    def iniciar(self):
        alarma_str = self.lcd_alarma.value()
        alarma = QtCore.QTime(alarma_str // 100, alarma_str % 100)

        self.timer.start(5000)

    def checar(self):
        try:
            tiempo = QtCore.QTime.currentTime()
            alarma_str = self.lcd_alarma.value()
            alarma = QtCore.QTime(alarma_str // 100, alarma_str % 100)
            if tiempo.hour() == alarma.hour() and tiempo.minute() == alarma.minute():
                cadena = "Despierta"
                msj = QtWidgets.QMessageBox()
                msj.setText(cadena)
                msj.exec_()
                pygame.mixer.music.load("the-synthwave-138196.wav")
                pygame.mixer.music.play()
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
