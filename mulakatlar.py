# Form implementation generated from reading ui file 'proje_son.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-image: url(\"C:/Users/ozmer/Desktop/week-2/zemin-buyuk.jpg\");\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 100, 291, 421))
        self.frame.setStyleSheet("QFrame QPushButton {\n"
"    background-color: white;\n"
"    \n"
"\n"
"\n"
"} ")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_ara = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_ara.setGeometry(QtCore.QRect(20, 100, 61, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_ara.setFont(font)
        self.pushButton_ara.setStyleSheet("QPushButton{\n"
"color:black;\n"
"background:white;\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"}")
        self.pushButton_ara.setObjectName("pushButton_ara")
        self.pushButton_tercih = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_tercih.setGeometry(QtCore.QRect(20, 330, 75, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_tercih.setFont(font)
        self.pushButton_tercih.setStyleSheet("QPushButton{\n"
"color:black;\n"
"background:white;\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"}")
        self.pushButton_tercih.setObjectName("pushButton_tercih")
        self.pushButton_exit = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_exit.setGeometry(QtCore.QRect(20, 370, 75, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setStyleSheet("QPushButton{\n"
"color:black;\n"
"background:white;\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"}")
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_gelmis = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_gelmis.setGeometry(QtCore.QRect(20, 170, 241, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_gelmis.setFont(font)
        self.pushButton_gelmis.setStyleSheet("QPushButton{\n"
"color:black;\n"
"background:white;\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"}")
        self.pushButton_gelmis.setObjectName("pushButton_gelmis")
        self.pushButton_gonderilmis = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_gonderilmis.setGeometry(QtCore.QRect(20, 220, 241, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_gonderilmis.setFont(font)
        self.pushButton_gonderilmis.setStyleSheet("QPushButton{\n"
"color:black;\n"
"background:white;\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"}")
        self.pushButton_gonderilmis.setObjectName("pushButton_gonderilmis")
        self.label_arama = QtWidgets.QLabel(parent=self.frame)
        self.label_arama.setGeometry(QtCore.QRect(20, 49, 201, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_arama.setFont(font)
        self.label_arama.setStyleSheet("QLabel{\n"
"color:black;\n"
"background:white;\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"}")
        self.label_arama.setObjectName("label_arama")
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(360, 170, 421, 351))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 421, 351))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("\n"
"font-weight:bold;\n"
"background:none")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;\n"
"font-size:36px;\n"
"font-weight:bold;\n"
"background:none")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_ara.setText(_translate("MainWindow", "ARA"))
        self.pushButton_tercih.setText(_translate("MainWindow", "TERCIHLER"))
        self.pushButton_exit.setText(_translate("MainWindow", "EXIT"))
        self.pushButton_gelmis.setText(_translate("MainWindow", "PROJESI GELMIS OLANLAR"))
        self.pushButton_gonderilmis.setText(_translate("MainWindow", "PROJESI GONDERILMIS OLANLAR"))
        self.label_arama.setText(_translate("MainWindow", "ARANACAK METNI GIRINIZ!"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ad -Soyad"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Proje Gelis Tarihi"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", " Proje Gonderilis Tarihi"))
        self.label.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><img src=\":/arkaplan/WhatsApp Image 2024-10-17 at 23.49.08.jpeg\"/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "MULAKATLAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
