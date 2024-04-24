import sys
from PyQt5 import uic, QtWidgets, QtCore
import pygame

qtCreatorFile = "E_03_Temporizador.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_iniciar.clicked.connect(self.iniciar)
        self.btn_detener.clicked.connect(self.detener)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.tiempo)
        pygame.mixer.init()

#En esta seccion se obtiene el valor de la cantidad de segundos para el temporizador
#Llama al metodo tiempo para el inicio del temporizador
#Inicia el temporizador que llamara al tiempo por cada segundo
    def iniciar(self):
        self.segundos = int(self.lineedit_tiempo.text())
        self.tiempo()
        self.timer.start(1000)

#Se detiene el tiempo al momento de presionar el boton de detener
    def detener(self):
        self.timer.stop()

#Decrementa en 1 la variable de segundos, ademas verifica si quedan segundos en el temporizador
#Si quedan se actualiza el texto para mostrar cuantos quedan
#Si no quedan, el temporizador se detiene y se establece el texto de tiempo terminado
#Cuando termina se reproduce un sonido
    def tiempo(self):
        self.segundos -= 1
        if self.segundos >= 0:
            self.txt_tiempo.setText(f"Tiempo restante: {self.segundos} segundos")
        else:
            self.timer.stop()
            self.txt_tiempo.setText("Tiempo terminado")
            pygame.mixer.music.load("the-synthwave-138196.wav")
            pygame.mixer.music.play()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
