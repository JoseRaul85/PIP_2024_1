import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E_JuegoGato.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.iniciar_juego()
        self.btn_reiniciar.clicked.connect(self.reiniciar)

    def iniciar_juego(self):
        self.turno = 'X'
        self.espacios = [' '] * 9

        self.btns = [
            self.btn1, self.btn2, self.btn3,
            self.btn4, self.btn5, self.btn6,
            self.btn7, self.btn8, self.btn9
        ]

        for btn in self.btns:
            btn.clicked.connect(self.casilla_seleccionada)

    def casilla_seleccionada(self):
        sender = self.sender()
        indice = self.btns.index(sender)

        if self.espacios[indice] == ' ':
            sender.setText(self.turno)
            self.espacios[indice] = self.turno
            if self.verificar_ganador():
                QtWidgets.QMessageBox.information(self, "Felicidades", f"El jugador {self.turno} ha ganado")
            elif ' ' not in self.espacios:
                QtWidgets.QMessageBox.information(self, "Empate", "El juego quedo en empate")
            else:
                self.turno = 'O' if self.turno == 'X' else 'X'

    def verificar_ganador(self):
        lineas_ganadoras = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

        for linea in lineas_ganadoras:
            a, b, c = linea
            if self.espacios[a] == self.espacios[b] == self.espacios[c] != ' ':
                return True
        return False

    def reiniciar(self):
        for btn in self.btns:
            btn.setText(' ')
        self.turno = 'X'
        self.espacios = [' '] * 9


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
