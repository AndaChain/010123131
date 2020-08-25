from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtQuickWidgets,QtGui
import sys

def window():
    app = QApplication(sys.argv)
    window = QMainWindow() 
    window.setGeometry(0,0,800,600) # set window size
    window.setWindowTitle("Calculator") # set window Title
    window.setMinimumSize(340,223) # set MinimumSize
    window.setWindowIcon(QtGui.QIcon("‪E:\\Picture\\54136.jpg"))
    window.show() # show window




    sys.exit(app.exec_())




a = 3+3j
print(a)