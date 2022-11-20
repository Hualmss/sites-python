from socket import BTPROTO_RFCOMM
from token import COMMENT
from tokenize import Comment
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os import system
import GPUtil




class MainApp(QMainWindow):
    numberFile=0
    totalFiles=0
    actualDir=''
    images = []
    def __init__(self, parent=None, *args):
        super(MainApp, self).__init__(parent=parent )
        #setMinimunSize(500,300) ancho alto, establece el tamaño minimo, por lo que no se puede achicar
        #setMaximunSise() igual que la anterior
        #setFixedSize() esta no se puede editar el tamaño de la pantalla, es decir es fijo
        self.setFixedSize(1100,700) 
        self.setWindowTitle("ClimateGan-DesktopApp")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)


        self.labe1 =  QLabel("Ingresar la dirección de la carpeta contenedora de imagenes", self.central_widget)
        self.labe1.adjustSize()
        self.labe2 =  QLabel("Ingresar la direccion de salida para las imagenes", self.central_widget)
        self.labe2.adjustSize()
        self.labe3 =  QLabel("Ingresar altura de la inundación", self.central_widget)
        self.labe3.adjustSize()
        
        
        



        self.enterDirectory = QLineEdit(self.central_widget)
        self.enterDirectory.setGeometry(0,0,300,28)
        self.enterDirectory.setPlaceholderText("ingresar direccion de imagenes")

        self.outDirectry =  QLineEdit(self.central_widget)
        self.outDirectry.setGeometry(0,0,300,28);
        self.outDirectry.setPlaceholderText("ingresar direccion de salida de imagenes")


        #self.flood =  QLineEdit(self.central_widget)
        #self.flood.setGeometry(0,0,300,28);
        #self.flood.setPlaceholderText("altura inundacion")
        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(QRect(40, 40, 300, 31))
        self.comboBox.addItem("0.5 m")
        self.comboBox.addItem("1 m")
        self.comboBox.addItem("1.25 m")
        
        self.comboBox.addItem("1.5 m")
        


        self.execute = QPushButton ("ejecutar", self.central_widget)
        self.selectFileIn = QPushButton ("seleccionar", self.central_widget)    #boton de seleccion de carpeta
        self.selectFileOut = QPushButton ("seleccionar", self.central_widget)    #boton de seleccion de carpeta
        
        self.next = QPushButton ("Siguiente >", self.central_widget)
        self.preview = QPushButton ("< Anterior", self.central_widget)

        self.CUDA = QPushButton ("verificar compatibilidad", self.central_widget)    #boton de seleccion de carpeta
        self.CUDA.setGeometry(0,0,300,28)
                
        s = QSize( 400, 5)
        self.label = QLabel(self) 
        self.pixmap = QPixmap('./imagen.jpeg') 
        self.tmp = QImage('./imagen3.png')
 
        pixi = QPixmap.fromImage(self.tmp).scaled(600, 450, 1,1)

        self.label.setPixmap(pixi)
        self.label.resize(800, 
                          400) 

        #ajustar coordenadas
        self.labe1.move(50, 40)
        self.enterDirectory.move(50,65)
        self.labe2.move(525, 40)
        self.outDirectry.move(525,65)
        
        self.labe3.move(50,115)
#        self.flood.move(50,125)
        self.comboBox.move(50,140)
        
        
        self.selectFileIn.move(360,65)
        self.selectFileOut.move(835,65)
        self.label.move(525,140)
        
        self.preview.move(675,550)
        self.next.move(770,550)

        self.CUDA.move(50,200)
        self.execute.move(50,250)
        

        

        


        #sms = "este es un sms"
        #self.btn = QPushButton("presioname con sms", self)#tenemos que crearle una señaol
        #self.btn_single = QPushButton("presioname nada", self)#tenemos que crearle una señaol


        #self.btn.setGeometry(0,0,150,40)
        #self.btn_single.setGeometry(200,0,15 0,40)


        #self.execute.clicked.connect(lambda: self.slot_params(sms))
        self.execute.clicked.connect(self.execButton)
        self.selectFileIn.clicked.connect(lambda: self.slot_whithout_params(1))
        self.selectFileOut.clicked.connect(lambda: self.slot_whithout_params(2))
        self.next.clicked.connect(self.nextImage)
        self.preview.clicked.connect(self.previewImage)
        self.CUDA.clicked.connect(lambda: self.showDialog())


    #cuando se crea un elemento por default mide 100x30
    
    def slot_params(self, sms):
        
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        print (file)
    def slot_whithout_params(self, tmp) :
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if tmp ==1 :#input images
            self.enterDirectory.setText(file)
            self.searchImages(file)
        else:#output images
            self.outDirectry.setText(file)
        print (file)
    
    def showDialog(self):
        # QMessageBox.warning(self, "Warning Dialog", "Peligro Alto Voltage")
        GPUtil.getAvailable()
        reply = QMessageBox.warning(self, "QMessageBox.critical()",
                "El computador no cuenta con una GPU Nvidia, la cual es requerida",
                QMessageBox.Ok | QMessageBox.Close )
        if reply == QMessageBox.Abort:
            print("Abortar la mision")
        elif reply == QMessageBox.Retry:
            print("Intentar nuevamente")
        else:
            print("Nada por ahora")



    def previewImage(self):
        if(self.numberFile -1 >= 0):
            self.tmp = QImage(self.actualDir + '/'+self.images[self.numberFile-1])
            pixi = QPixmap.fromImage(self.tmp).scaled(450, 450, 1,1)
            self.label.setPixmap(pixi)
            self.label.resize(600, 
                        400) 
            self.numberFile = self.numberFile-1
        else:
            self.numberFile = self.totalFiles-1
            self.tmp = QImage(self.actualDir + '/'+self.images[self.totalFiles-1])
            pixi = QPixmap.fromImage(self.tmp).scaled(450, 450, 1,1)
            self.label.setPixmap(pixi)
            self.label.resize(600, 
                        400) 

    def nextImage(self):
      
       if(self.numberFile +1 <self.totalFiles):
            self.tmp = QImage(self.actualDir + '/'+self.images[self.numberFile+1])
            pixi = QPixmap.fromImage(self.tmp).scaled(450, 450, 1,1)
            self.label.setPixmap(pixi)
            self.label.resize(600, 
                        400) 
            self.numberFile = self.numberFile+1
       else:
            self.numberFile = 0
            self.tmp = QImage(self.actualDir + '/'+self.images[0])
            pixi = QPixmap.fromImage(self.tmp).scaled(450, 450, 1,1)
            self.label.setPixmap(pixi)
            self.label.resize(600, 
                        400) 
            
            


    def searchImages(self, dir):
        files = os.listdir(dir)	 
        self.totalFiles = len(files)
        self.actualDir=dir
        i = 0

        for v in files:
            if(v.find('jpg')!=-1 or v.find('png')!=-1 or v.find('jpeg')!=-1):
                self.images.append(v)
        print(self.images)
        for v in files:
            if(v.find('jpg')!=-1 or v.find('png')!=-1 or v.find('jpeg')!=-1):
                print(dir+ '/'+v)
                self.tmp = QImage(dir + '/'+v)
                pixi = QPixmap.fromImage(self.tmp).scaled(450, 450, 1,1)
                self.label.setPixmap(pixi)
                self.label.resize(600, 
                          400) 
                print ("valor: %s" %v)
                break
                i = i +1
        self.numberFile = i
        print (self.numberFile)
                
                
    def execButton(self):
        cadena = '--version'
        print(cadena)
        print(system('python '+cadena))






if __name__ =='__main__':    
    
    
    app = QApplication([])  #Inciaa la app
    window = MainApp()      #Se establece la ventana
    window.show()           #Se muestra la venta
    app.exec_()             #Se ejecuta la app


