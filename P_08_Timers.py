import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P_08_Timers.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_iniciar.clicked.connect(self.iniciar)
        self.btn_iniciar_2.clicked.connect(self.iniciar2)
        self.segundo = QtCore.QTimer()
        self.segundo.timeout.connect(self.contar)

    def iniciar(self):
        try:
            import time as t
            n = int(self.txt_numero.text())
            print(n)
            for i in range(n):
                self.txt_contador.setText(str(i + 1))
                t.sleep(0.5)
                print(i + 1)
        except Exception as e:
            print(f"Error in iniciar: {e}")

    def iniciar2(self):
        try:
            self.num = int(self.txt_numero_2.text())
            print(self.num)
            self.segundo.start(100)
            self.cont = 1
            self.txt_contador_2.setText("1")
        except Exception as e:
            print(f"Error in iniciar2: {e}")

    def contar(self):
        try:
            if self.cont < self.num:
                self.cont += 1
                self.txt_contador_2.setText(str(self.cont))
            else:
                self.segundo.stop()
        except Exception as e:
            print(f"Error in contar: {e}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
