import serial
import statistics
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QStandardItem, QStandardItemModel

#Importar metodos para los botones
from Metodos.Normalizar import normalizar


# Cargar la interfaz gráfica desde el archivo .ui
qtCreatorFile = "UI_Proyecto3.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Configurar la conexión serial con Arduino
        self.arduino = serial.Serial('COM3', 9600, timeout=1)

        # Crear el modelo de lista para mostrar los datos
        self.list_model = QStandardItemModel()

        # Obtener la referencia al QListView
        self.list_view = self.listView

        # Establecer el modelo de lista en el QListView
        self.list_view.setModel(self.list_model)

        # Conectar el botón "Leer datos" con la función que lee los valores del potenciómetro
        self.btnStart.clicked.connect(self.leer_datos)
        self.btnNormalizacion.clicked.connect(self.leer_datos)

    def leer_datos(self):
        # Leer 30 valores del potenciómetro desde Arduino
        valores = []
        while len(valores) < 30:
            lectura = self.arduino.readline().decode().strip()
            if lectura:
                valores = list(map(int, lectura.strip().rstrip(',').split(',')))

        print("Valores recibidos:", valores)

        #Area para los metodos
        valores_normalizados = normalizar(valores)

        # Calcular la moda, media, mediana, mayor y menor
        moda = statistics.mode(valores)
        media = statistics.mean(valores)
        mediana = statistics.median(valores)
        mayor = max(valores)
        menor = min(valores)

        # Limpiar el modelo de lista
        self.list_model.clear()

        # Agregar los datos al modelo de lista
        self.list_model.appendRow(QStandardItem("Valores recibidos: " + str(valores)))
        self.list_model.appendRow(QStandardItem("Moda: " + str(moda)))
        self.list_model.appendRow(QStandardItem("Media: " + str(media)))
        self.list_model.appendRow(QStandardItem("Mediana: " + str(mediana)))
        self.list_model.appendRow(QStandardItem("Mayor: " + str(mayor)))
        self.list_model.appendRow(QStandardItem("Menor: " + str(menor)))
        self.list_model.appendRow(QStandardItem("Valores normalizados: " + str(valores_normalizados)))

        #Acion de los botones


    def closeEvent(self, event):
        # Cerrar la conexión serial con Arduino al cerrar la aplicación
        self.arduino.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
