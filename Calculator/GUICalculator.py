# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(315, 190)
        MainWindow.setMinimumSize(QtCore.QSize(315, 190))
        MainWindow.setMaximumSize(QtCore.QSize(315, 190))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.seven = QtWidgets.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(0, 70, 81, 31))
        self.seven.setStyleSheet("background-color: rgb(189, 189, 189);\n"
"font: 57 16pt \"Chakra Petch\";")
        self.seven.setObjectName("seven")
        self.eight = QtWidgets.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(80, 70, 81, 31))
        self.eight.setStyleSheet("background-color: rgb(189, 189, 189);\n"
"font: 57 16pt \"Chakra Petch\";")
        self.eight.setObjectName("eight")
        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(0, 100, 81, 31))
        self.four.setStyleSheet("background-color: rgb(189, 189, 189);\n"
"font: 57 16pt \"Chakra Petch\";")
        self.four.setObjectName("four")
        self.five = QtWidgets.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(80, 100, 81, 31))
        self.five.setStyleSheet("background-color: rgb(189, 189, 189);\n"
"font: 57 16pt \"Chakra Petch\";")
        self.five.setObjectName("five")
        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(0, 130, 81, 31))
        self.one.setStyleSheet("background-color: rgb(189, 189, 189);\n"
"font: 57 16pt \"Chakra Petch\";")
        self.one.setObjectName("one")
        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(80, 130, 81, 31))
        self.two.setStyleSheet("background-color: rgb(189, 189, 189);\n"
"font: 57 16pt \"Chakra Petch\";")
        self.two.setObjectName("two")
        self.nine = QtWidgets.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(160, 70, 81, 31))
        self.nine.setStyleSheet("background-color: rgb(189, 189, 189);\n"
"font: 57 16pt \"Chakra Petch\";")
        self.nine.setObjectName("nine")
        self.six = QtWidgets.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(160, 100, 81, 31))
        self.six.setStyleSheet("background-color: rgb(189, 189, 189);\n"
"font: 57 16pt \"Chakra Petch\";")
        self.six.setObjectName("six")
        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(160, 130, 81, 31))
        self.three.setStyleSheet("background-color: rgb(189, 189, 189);\n"
"font: 57 16pt \"Chakra Petch\";")
        self.three.setObjectName("three")
        self.zero = QtWidgets.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(0, 160, 81, 31))
        self.zero.setStyleSheet("background-color: rgb(189, 189, 189);\n"
"font: 57 16pt \"Chakra Petch\";")
        self.zero.setObjectName("zero")
        self.divided = QtWidgets.QPushButton(self.centralwidget)
        self.divided.setGeometry(QtCore.QRect(234, 160, 81, 31))
        self.divided.setMinimumSize(QtCore.QSize(81, 31))
        self.divided.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(255, 255, 255);\n"
"font: 57 16pt \"Chakra Petch\";")
        self.divided.setObjectName("divided")
        self.muti = QtWidgets.QPushButton(self.centralwidget)
        self.muti.setGeometry(QtCore.QRect(240, 130, 75, 31))
        self.muti.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(255, 255, 255);\n"
"font: 57 16pt \"Chakra Petch\";")
        self.muti.setObjectName("muti")
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(240, 100, 75, 31))
        self.minus.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(255, 255, 255);\n"
"font: 57 16pt \"Chakra Petch\";")
        self.minus.setObjectName("minus")
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(240, 70, 75, 31))
        self.plus.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(255, 255, 255);\n"
"font: 57 16pt \"Chakra Petch\";")
        self.plus.setObjectName("plus")
        self.solve = QtWidgets.QPushButton(self.centralwidget)
        self.solve.setGeometry(QtCore.QRect(240, 0, 75, 41))
        self.solve.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"font: 57 16pt \"Chakra Petch\";")
        self.solve.setObjectName("solve")
        self.display = QtWidgets.QTextBrowser(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(0, 0, 241, 41))
        self.display.setStyleSheet("")
        self.display.setObjectName("display")
        self.dot = QtWidgets.QPushButton(self.centralwidget)
        self.dot.setGeometry(QtCore.QRect(80, 160, 81, 31))
        self.dot.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(255, 255, 255);\n"
"font: 57 16pt \"Chakra Petch\";")
        self.dot.setObjectName("dot")
        self.delete_all = QtWidgets.QPushButton(self.centralwidget)
        self.delete_all.setGeometry(QtCore.QRect(80, 40, 81, 31))
        self.delete_all.setStyleSheet("background-color: rgb(189, 189, 189);\n"
"font: 57 16pt \"Chakra Petch\";")
        self.delete_all.setObjectName("delete_all")
        self.delete_step = QtWidgets.QPushButton(self.centralwidget)
        self.delete_step.setGeometry(QtCore.QRect(0, 40, 81, 31))
        self.delete_step.setStyleSheet("background-color: rgb(189, 189, 189);\n"
"font: 57 16pt \"Chakra Petch\";")
        self.delete_step.setObjectName("delete_step")
        self.power = QtWidgets.QPushButton(self.centralwidget)
        self.power.setGeometry(QtCore.QRect(160, 160, 81, 31))
        self.power.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(255, 255, 255);\n"
"font: 57 16pt \"Chakra Petch\";")
        self.power.setObjectName("power")
        self.close_bracket = QtWidgets.QPushButton(self.centralwidget)
        self.close_bracket.setGeometry(QtCore.QRect(240, 40, 75, 31))
        self.close_bracket.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(255, 255, 255);\n"
"font: 57 16pt \"Chakra Petch\";")
        self.close_bracket.setObjectName("close_bracket")
        self.open_bracket = QtWidgets.QPushButton(self.centralwidget)
        self.open_bracket.setGeometry(QtCore.QRect(160, 40, 81, 31))
        self.open_bracket.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(255, 255, 255);\n"
"font: 57 16pt \"Chakra Petch\";")
        self.open_bracket.setObjectName("open_bracket")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.four.setText(_translate("MainWindow", "4"))
        self.five.setText(_translate("MainWindow", "5"))
        self.one.setText(_translate("MainWindow", "1"))
        self.two.setText(_translate("MainWindow", "2"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.six.setText(_translate("MainWindow", "6"))
        self.three.setText(_translate("MainWindow", "3"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.divided.setText(_translate("MainWindow", "/"))
        self.muti.setText(_translate("MainWindow", "*"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.solve.setText(_translate("MainWindow", "="))
        self.display.setHtml(_translate("MainWindow", ""))
        self.dot.setText(_translate("MainWindow", "."))
        self.delete_all.setText(_translate("MainWindow", "CE"))
        self.delete_step.setText(_translate("MainWindow", "<x"))
        self.power.setText(_translate("MainWindow", "^"))
        self.close_bracket.setText(_translate("MainWindow", ")"))
        self.open_bracket.setText(_translate("MainWindow", "("))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())