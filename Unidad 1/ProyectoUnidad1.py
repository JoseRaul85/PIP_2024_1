import sys
from PyQt5 import uic, QtWidgets
import statistics
qtCreatorFile = "ProyectoUnidad1.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_resultado.clicked.connect(self.sumar)
        self.btn_resultado.clicked.connect(self.media)
        self.btn_resultado.clicked.connect(self.calcularmoda)
        self.btn_resultado.clicked.connect(self.mediana)
        self.btn_resultado.clicked.connect(self.valorMayor)
        self.btn_resultado.clicked.connect(self.valorMenor)
        self.btn_resultado.clicked.connect(self.desviacionEstandar)
        self.btn_resultado.clicked.connect(self.varianza)

        self.txt_desviacion.setEnabled(False)
        self.txt_media.setEnabled(False)
        self.txt_mediana.setEnabled(False)
        self.txt_moda.setEnabled(False)
        self.txt_suma.setEnabled(False)
        self.txt_valormayor.setEnabled(False)
        self.txt_valormenor.setEnabled(False)
        self.txt_varianza.setEnabled(False)

    def sumar(self):
        try:
            numeros =  self.txt_numero.text()
            lista = numeros.split(", ")
            print(lista)
            lista_en_numeros = [int(i) for i in lista]
            print(lista_en_numeros)
            suma = sum(lista_en_numeros)
            self.txt_suma.setText(str(suma))
        except Exception as errorsumar:
            print(errorsumar)

    def media(self):
        try:
            numeros =  self.txt_numero.text()
            lista = numeros.split(", ")
            print(lista)
            lista_en_numeros = [int(i) for i in lista]
            print(lista_en_numeros)
            suma = sum(lista_en_numeros)
            tamano = len(lista_en_numeros)
            promedio = suma / tamano
            self.txt_media.setText(str(promedio))
        except Exception as errormedia:
            print(errormedia)

    def calcularmoda(self):
        try:
            numeros = self.txt_numero.text()
            lista = numeros.split(", ")
            conteo = {}
            for elemento in lista:
                if elemento in conteo:
                    conteo[elemento] += 1
                else:
                    conteo[elemento] = 1

            max_repeticiones = max(conteo.values())
            repeticiones = [numero for numero, repeticiones in conteo.items() if repeticiones == max_repeticiones]
            print(f"El numero mas repetido es: {repeticiones} se repite {max_repeticiones} veces")
            self.txt_moda.setText(str(f"{repeticiones} se repite {max_repeticiones} veces"))
        except Exception as error:
            print(error)

    def mediana(self):
        try:
            numeros = self.txt_numero.text()
            lista = numeros.split(", ")
            n = len(lista)
            nueva_lista = lista.copy()
            parLista = n % 2
            for i in range(n):
                for j in range(0, n - i - 1):
                    if nueva_lista[j] > nueva_lista[j + 1]:
                        nueva_lista[j], nueva_lista[j + 1] = nueva_lista[j + 1], nueva_lista[j]
            if parLista == 1:
                medianaPrNum = int((n / 2))
                resultado = nueva_lista[medianaPrNum]
                self.txt_mediana.setText(str(resultado))
            else:
                medianaPrNum = int(n / 2)
                medianaSdNum = int((n / 2) - 1)
                mostrarNumeroUno = int(nueva_lista[medianaPrNum])
                mostrarNumeroDos = int(nueva_lista[medianaSdNum])
                division = float((mostrarNumeroUno + mostrarNumeroDos) / 2)
                self.txt_mediana.setText(str(division))
            valormayor = nueva_lista[n - 1]
            return valormayor

        except Exception as errormediana:
            print(errormediana)

    def valorMayor(self):
        try:
            valormayor = self.mediana()
            self.txt_valormayor.setText(str(valormayor))
        except Exception as errorvmayor:
            print(errorvmayor)

    def valorMenor(self):
        try:
            numeros = self.txt_numero.text()
            lista = numeros.split(", ")
            minimo = min(lista)
            self.txt_valormenor.setText(str(minimo))
        except Exception as errorvmenor:
            print(errorvmenor)

    def desviacionEstandar(self):
        try:
            numeros = self.txt_numero.text()
            lista = [float(numero) for numero in numeros.split(", ")]
            desviacion = statistics.stdev(lista)
            self.txt_desviacion.setText(str(desviacion))
        except Exception as errordesviacion:
            print(errordesviacion)

    def varianza(self):
        try:
            numeros = self.txt_numero.text()
            lista = [float(numero) for numero in numeros.split(", ")]
            varianza = statistics.variance(lista)
            self.txt_varianza.setText(str(varianza))
        except Exception as errorvarianza:
            print(errorvarianza)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
