# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_Prod.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1232, 773)
        Form.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.784091, y1:0.102, x2:0, y2:1, stop:0.232955 rgba(189, 44, 161, 255), stop:0.596591 rgba(28, 73, 236, 255))")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1231, 771))
        self.frame.setStyleSheet("background-color:red;\n"
"background-color: qlineargradient(spread:pad, x1:0.784091, y1:0.102, x2:0, y2:1, stop:0.232955 rgba(189, 44, 161, 255), stop:0.596591 rgba(28, 73, 236, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.insideForm = QtWidgets.QFrame(self.frame)
        self.insideForm.setStyleSheet("background-color: rgb(227, 227, 227);\n"
"border-radius:10px;\n"
"")
        self.insideForm.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.insideForm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.insideForm.setObjectName("insideForm")
        self.menuForm = QtWidgets.QFrame(self.insideForm)
        self.menuForm.setGeometry(QtCore.QRect(0, 0, 291, 757))
        self.menuForm.setMaximumSize(QtCore.QSize(300, 16777215))
        self.menuForm.setStyleSheet("background-color: rgb(60, 91, 158);\n"
"border-radius:10px;")
        self.menuForm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menuForm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menuForm.setObjectName("menuForm")
        self.logo = QtWidgets.QLabel(self.menuForm)
        self.logo.setGeometry(QtCore.QRect(-140, -50, 561, 241))
        self.logo.setStyleSheet("image: url(:/logo/C:/Users/amadi/Downloads/image-removebg-preview.png);")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.btnAlgoritm = QtWidgets.QPushButton(self.menuForm)
        self.btnAlgoritm.setGeometry(QtCore.QRect(80, 330, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btnAlgoritm.setFont(font)
        self.btnAlgoritm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAlgoritm.setStyleSheet("background-color: rgb(227, 227, 227);\n"
"color: rgb(0, 0, 0);\n"
"text-align:center;\n"
"padding: 0.8em 1.5em;\n"
"border-radious:2px;\n"
"text-decoration: none;\n"
"font-size: 1em;\n"
"border-radius: 5px;\n"
"align-item:center;\n"
"border:2px solid rgb(55, 75, 108);\n"
"font-weight:bold;")
        self.btnAlgoritm.setObjectName("btnAlgoritm")
        self.btnExit = QtWidgets.QPushButton(self.menuForm)
        self.btnExit.setGeometry(QtCore.QRect(80, 390, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btnExit.setFont(font)
        self.btnExit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnExit.setStyleSheet("background-color: rgb(227, 227, 227);\n"
"color: rgb(0, 0, 0);\n"
"text-align:center;\n"
"padding: 0.8em 1.5em;\n"
"border-radious:2px;\n"
"text-decoration: none;\n"
"font-size: 1em;\n"
"border-radius: 5px;\n"
"align-item:center;\n"
"border:2px solid rgb(55, 75, 108);\n"
"font-weight:bold;")
        self.btnExit.setObjectName("btnExit")
        self.btnDashboard = QtWidgets.QPushButton(self.menuForm)
        self.btnDashboard.setGeometry(QtCore.QRect(80, 150, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btnDashboard.setFont(font)
        self.btnDashboard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDashboard.setStyleSheet("background-color: rgb(227, 227, 227);\n"
"color: rgb(0, 0, 0);\n"
"text-align:center;\n"
"border:2px solid rgb(55, 75, 108);\n"
"padding: 0.8em 1.5em;\n"
"border-radious:2px;\n"
"text-decoration: none;\n"
"font-size: 1em;\n"
"border-radius: 10px;\n"
"align-item:center;\n"
"font-weight:bold;")
        self.btnDashboard.setObjectName("btnDashboard")
        self.btnScrapping = QtWidgets.QPushButton(self.menuForm)
        self.btnScrapping.setGeometry(QtCore.QRect(80, 210, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btnScrapping.setFont(font)
        self.btnScrapping.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnScrapping.setStyleSheet("background-color: rgb(227, 227, 227);\n"
"color: rgb(0, 0, 0);\n"
"text-align:center;\n"
"border:2px solid rgb(55, 75, 108);\n"
"padding: 0.8em 1.5em;\n"
"border-radious:2px;\n"
"text-decoration: none;\n"
"font-size: 1em;\n"
"border-radius: 10px;\n"
"align-item:center;\n"
"font-weight:bold;")
        self.btnScrapping.setObjectName("btnScrapping")
        self.btnProduct = QtWidgets.QPushButton(self.menuForm)
        self.btnProduct.setGeometry(QtCore.QRect(80, 270, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btnProduct.setFont(font)
        self.btnProduct.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnProduct.setStyleSheet("background-color: rgb(227, 227, 227);\n"
"color: rgb(0, 0, 0);\n"
"text-align:center;\n"
"padding: 0.8em 1.5em;\n"
"border-radious:2px;\n"
"text-decoration: none;\n"
"font-size: 1em;\n"
"border-radius: 5px;\n"
"align-item:center;\n"
"border:2px solid rgb(55, 75, 108);\n"
"font-weight:bold;")
        self.btnProduct.setObjectName("btnProduct")
        self.logo.raise_()
        self.btnAlgoritm.raise_()
        self.btnExit.raise_()
        self.btnScrapping.raise_()
        self.btnProduct.raise_()
        self.btnDashboard.raise_()
        self.label = QtWidgets.QLabel(self.insideForm)
        self.label.setGeometry(QtCore.QRect(530, 10, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(35)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(60, 91, 158);")
        self.label.setObjectName("label")
        self.btnDelete = QtWidgets.QPushButton(self.insideForm)
        self.btnDelete.setGeometry(QtCore.QRect(620, 640, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btnDelete.setFont(font)
        self.btnDelete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDelete.setStyleSheet("background-color: rgb(227, 227, 227);\n"
"color: rgb(0, 0, 0);\n"
"text-align:center;\n"
"border:2px solid rgb(55, 75, 108);\n"
"padding: 0.8em 1.5em;\n"
"border-radious:2px;\n"
"text-decoration: none;\n"
"font-size: 1em;\n"
"border-radius: 10px;\n"
"align-item:center;\n"
"font-weight:bold;")
        self.btnDelete.setObjectName("btnDelete")
        self.btnAdd = QtWidgets.QPushButton(self.insideForm)
        self.btnAdd.setGeometry(QtCore.QRect(440, 640, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btnAdd.setFont(font)
        self.btnAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAdd.setStyleSheet("background-color: rgb(227, 227, 227);\n"
"color: rgb(0, 0, 0);\n"
"text-align:center;\n"
"border:2px solid rgb(55, 75, 108);\n"
"padding: 0.8em 1.5em;\n"
"border-radious:2px;\n"
"text-decoration: none;\n"
"font-size: 1em;\n"
"border-radius: 10px;\n"
"align-item:center;\n"
"font-weight:bold;")
        self.btnAdd.setObjectName("btnAdd")
        self.btnupdate = QtWidgets.QPushButton(self.insideForm)
        self.btnupdate.setGeometry(QtCore.QRect(800, 640, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btnupdate.setFont(font)
        self.btnupdate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnupdate.setStyleSheet("background-color: rgb(227, 227, 227);\n"
"color: rgb(0, 0, 0);\n"
"text-align:center;\n"
"border:2px solid rgb(55, 75, 108);\n"
"padding: 0.8em 1.5em;\n"
"border-radious:2px;\n"
"text-decoration: none;\n"
"font-size: 1em;\n"
"border-radius: 10px;\n"
"align-item:center;\n"
"font-weight:bold;")
        self.btnupdate.setObjectName("btnupdate")
        self.tVProduct = QtWidgets.QTableView(self.insideForm)
        self.tVProduct.setGeometry(QtCore.QRect(320, 90, 841, 481))
        self.tVProduct.setGridStyle(QtCore.Qt.DashDotLine)
        self.tVProduct.setObjectName("tVProduct")
        self.horizontalLayout.addWidget(self.insideForm)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnAlgoritm.setText(_translate("Form", "Algorithm"))
        self.btnExit.setText(_translate("Form", "Exit"))
        self.btnDashboard.setText(_translate("Form", "Dashboard"))
        self.btnScrapping.setText(_translate("Form", "Scrapping"))
        self.btnProduct.setText(_translate("Form", "Products"))
        self.label.setText(_translate("Form", "Products"))
        self.btnDelete.setText(_translate("Form", "Delete"))
        self.btnAdd.setText(_translate("Form", "Add"))
        self.btnupdate.setText(_translate("Form", "Update"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())