import sys
import random
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QTimer

qtCreatorFile = "E_Memorama.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.init_game()
        self.init_memorama()
        self.btn_reiniciar.clicked.connect(self.reiniciar_juego)

    def init_game(self):
        self.turno = 0
        self.pares_encontrados = 0
        self.cartas_volteadas = []

    def init_memorama(self):
        self.signos = ['$', '#', '%'] * 2
        random.shuffle(self.signos)
        self.casillas = [
            self.btn1, self.btn2, self.btn3,
            self.btn4, self.btn5, self.btn6
        ]

        for casilla in self.casillas:
            casilla.clicked.connect(self.casilla_seleccionada)

    def casilla_seleccionada(self):
        if len(self.cartas_volteadas) < 2:
            sender = self.sender()
            index = self.casillas.index(sender)
            sender.setText(self.signos[index])
            sender.setDisabled(True)
            self.cartas_volteadas.append((sender, self.signos[index]))

            if len(self.cartas_volteadas) == 2:
                QTimer.singleShot(500, self.verificar_pares)

    def verificar_pares(self):
        if self.cartas_volteadas[0][1] == self.cartas_volteadas[1][1]:
            self.cartas_volteadas[0][0].setDisabled(True)
            self.cartas_volteadas[1][0].setDisabled(True)
            self.pares_encontrados += 1
            if self.pares_encontrados == 3:
                QtWidgets.QMessageBox.information(self, "Felicidades", "Encontraste los pares :D")
        else:
            self.cartas_volteadas[0][0].setText('')
            self.cartas_volteadas[1][0].setText('')
            self.cartas_volteadas[0][0].setEnabled(True)
            self.cartas_volteadas[1][0].setEnabled(True)
        self.cartas_volteadas = []

    def reiniciar_juego(self):
        self.init_game()
        for casilla in self.casillas:
            casilla.setEnabled(True)
            casilla.setText('')
            casilla.clicked.disconnect()
        self.init_memorama()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
