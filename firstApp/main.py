from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(MainApp, self).__init__(parent=parent )
        #setMinimunSize(500,300) ancho alto, establece el tamaño minimo, por lo que no se puede achicar
        #setMaximunSise() igual que la anterior
        #setFixedSize() esta no se puede editar el tamaño de la pantalla, es decir es fijo
        self.setMinimumSize(500,300) 
        self.setWindowTitle("ClimateGan-DesktopApp")
        

        label = QLabel("Primer Label")



if __name__ =='__main__':    
    
    
    app = QApplication([])  #Inciaa la app
    window = MainApp()      #Se establece la ventana
    window.show()           #Se muestra la venta
    app.exec_()             #Se ejecuta la app


 