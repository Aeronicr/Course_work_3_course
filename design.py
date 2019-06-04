# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(938, 567)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Main = QtWidgets.QFrame(self.centralwidget)
        self.Main.setGeometry(QtCore.QRect(-10, -10, 951, 581))
        self.Main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Main.setObjectName("Main")
        self.label = QtWidgets.QLabel(self.Main)
        self.label.setGeometry(QtCore.QRect(6, -10, 941, 601))
        self.label.setStyleSheet("background-image: url(:/bac_image/cabinet.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_patients = QtWidgets.QPushButton(self.Main)
        self.pushButton_patients.setGeometry(QtCore.QRect(290, 200, 371, 41))
        self.pushButton_patients.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_patients.setObjectName("pushButton_patients")
        self.label_2 = QtWidgets.QLabel(self.Main)
        self.label_2.setGeometry(QtCore.QRect(160, 20, 661, 181))
        self.label_2.setStyleSheet("background-image: url(:/bac_image/logo.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_doctors = QtWidgets.QPushButton(self.Main)
        self.pushButton_doctors.setGeometry(QtCore.QRect(290, 250, 371, 41))
        self.pushButton_doctors.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_doctors.setObjectName("pushButton_doctors")
        self.pushButton_medicines = QtWidgets.QPushButton(self.Main)
        self.pushButton_medicines.setGeometry(QtCore.QRect(290, 300, 371, 41))
        self.pushButton_medicines.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_medicines.setObjectName("pushButton_medicines")
        self.pushButton_visits = QtWidgets.QPushButton(self.Main)
        self.pushButton_visits.setGeometry(QtCore.QRect(290, 350, 371, 41))
        self.pushButton_visits.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_visits.setObjectName("pushButton_visits")
        self.pushButton_discount = QtWidgets.QPushButton(self.Main)
        self.pushButton_discount.setGeometry(QtCore.QRect(290, 400, 371, 41))
        self.pushButton_discount.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_discount.setObjectName("pushButton_discount")
        self.pushButton_close = QtWidgets.QPushButton(self.Main)
        self.pushButton_close.setGeometry(QtCore.QRect(290, 450, 371, 41))
        self.pushButton_close.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_medicines_6 = QtWidgets.QPushButton(self.Main)
        self.pushButton_medicines_6.setGeometry(QtCore.QRect(830, 480, 71, 61))
        self.pushButton_medicines_6.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_medicines_6.setObjectName("pushButton_medicines_6")
        self.Edit_visits = QtWidgets.QFrame(self.centralwidget)
        self.Edit_visits.setGeometry(QtCore.QRect(-21, -10, 981, 591))
        self.Edit_visits.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Edit_visits.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Edit_visits.setObjectName("Edit_visits")
        self.label_36 = QtWidgets.QLabel(self.Edit_visits)
        self.label_36.setGeometry(QtCore.QRect(16, 5, 951, 591))
        self.label_36.setStyleSheet("background-image: url(:/bac_image/cabinet.jpg);")
        self.label_36.setText("")
        self.label_36.setObjectName("label_36")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.Edit_visits)
        self.lineEdit_5.setGeometry(QtCore.QRect(300, 20, 331, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.Edit_visits)
        self.lineEdit_6.setGeometry(QtCore.QRect(300, 70, 331, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.Edit_visits)
        self.lineEdit_18.setGeometry(QtCore.QRect(300, 120, 331, 31))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.Edit_visits)
        self.lineEdit_26.setGeometry(QtCore.QRect(300, 170, 331, 31))
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.Edit_visits)
        self.lineEdit_27.setGeometry(QtCore.QRect(300, 220, 331, 31))
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.Edit_visits)
        self.lineEdit_28.setGeometry(QtCore.QRect(300, 270, 331, 31))
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.label_37 = QtWidgets.QLabel(self.Edit_visits)
        self.label_37.setGeometry(QtCore.QRect(86, 20, 191, 31))
        self.label_37.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.Edit_visits)
        self.label_38.setGeometry(QtCore.QRect(80, 70, 201, 31))
        self.label_38.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.Edit_visits)
        self.label_39.setGeometry(QtCore.QRect(80, 120, 201, 31))
        self.label_39.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.Edit_visits)
        self.label_40.setGeometry(QtCore.QRect(80, 320, 201, 31))
        self.label_40.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.Edit_visits)
        self.label_41.setGeometry(QtCore.QRect(80, 170, 201, 31))
        self.label_41.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.Edit_visits)
        self.label_42.setGeometry(QtCore.QRect(80, 220, 201, 31))
        self.label_42.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.Edit_visits)
        self.label_43.setGeometry(QtCore.QRect(80, 270, 201, 31))
        self.label_43.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_43.setObjectName("label_43")
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.Edit_visits)
        self.calendarWidget_2.setGeometry(QtCore.QRect(300, 320, 331, 191))
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.Edit_visits)
        self.tableWidget_4.setGeometry(QtCore.QRect(680, 30, 256, 141))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(2)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        self.tableWidget_5 = QtWidgets.QTableWidget(self.Edit_visits)
        self.tableWidget_5.setGeometry(QtCore.QRect(680, 190, 256, 161))
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(2)
        self.tableWidget_5.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        self.tableWidget_6 = QtWidgets.QTableWidget(self.Edit_visits)
        self.tableWidget_6.setGeometry(QtCore.QRect(680, 370, 256, 171))
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(2)
        self.tableWidget_6.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        self.pushButton_35 = QtWidgets.QPushButton(self.Edit_visits)
        self.pushButton_35.setGeometry(QtCore.QRect(124, 530, 101, 31))
        self.pushButton_35.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_36 = QtWidgets.QPushButton(self.Edit_visits)
        self.pushButton_36.setGeometry(QtCore.QRect(450, 530, 121, 31))
        self.pushButton_36.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton_37 = QtWidgets.QPushButton(self.Edit_visits)
        self.pushButton_37.setGeometry(QtCore.QRect(120, 530, 101, 31))
        self.pushButton_37.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_37.setObjectName("pushButton_37")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(270, 10, 120, 80))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(410, 10, 120, 80))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(550, 10, 120, 80))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(690, 10, 120, 80))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(820, 10, 120, 80))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setGeometry(QtCore.QRect(10, 100, 120, 80))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.frame_9 = QtWidgets.QFrame(self.centralwidget)
        self.frame_9.setGeometry(QtCore.QRect(140, 100, 120, 80))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.Patients = QtWidgets.QFrame(self.centralwidget)
        self.Patients.setGeometry(QtCore.QRect(-11, -11, 951, 581))
        self.Patients.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Patients.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Patients.setObjectName("Patients")
        self.label_3 = QtWidgets.QLabel(self.Patients)
        self.label_3.setGeometry(QtCore.QRect(0, 2, 951, 581))
        self.label_3.setStyleSheet("background-image: url(:/bac_image/cabinet.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.tableWidget_patients = QtWidgets.QTableWidget(self.Patients)
        self.tableWidget_patients.setGeometry(QtCore.QRect(110, 70, 741, 391))
        self.tableWidget_patients.setObjectName("tableWidget_patients")
        self.tableWidget_patients.setColumnCount(6)
        self.tableWidget_patients.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_patients.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_patients.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_patients.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_patients.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_patients.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_patients.setHorizontalHeaderItem(5, item)
        self.label_4 = QtWidgets.QLabel(self.Patients)
        self.label_4.setGeometry(QtCore.QRect(420, 30, 111, 31))
        self.label_4.setStyleSheet("font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_4.setObjectName("label_4")
        self.pushButton_pat_show = QtWidgets.QPushButton(self.Patients)
        self.pushButton_pat_show.setGeometry(QtCore.QRect(764, 520, 121, 31))
        self.pushButton_pat_show.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_pat_show.setObjectName("pushButton_pat_show")
        self.pushButton_pat_add = QtWidgets.QPushButton(self.Patients)
        self.pushButton_pat_add.setGeometry(QtCore.QRect(620, 520, 121, 31))
        self.pushButton_pat_add.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_pat_add.setObjectName("pushButton_pat_add")
        self.pushButton_pat_edit = QtWidgets.QPushButton(self.Patients)
        self.pushButton_pat_edit.setGeometry(QtCore.QRect(480, 520, 121, 31))
        self.pushButton_pat_edit.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_pat_edit.setObjectName("pushButton_pat_edit")
        self.pushButton_pat_del = QtWidgets.QPushButton(self.Patients)
        self.pushButton_pat_del.setGeometry(QtCore.QRect(340, 520, 121, 31))
        self.pushButton_pat_del.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_pat_del.setObjectName("pushButton_pat_del")
        self.pushButton_pat_search = QtWidgets.QPushButton(self.Patients)
        self.pushButton_pat_search.setGeometry(QtCore.QRect(200, 520, 121, 31))
        self.pushButton_pat_search.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_pat_search.setObjectName("pushButton_pat_search")
        self.pushButton_pat_menu = QtWidgets.QPushButton(self.Patients)
        self.pushButton_pat_menu.setGeometry(QtCore.QRect(60, 520, 121, 31))
        self.pushButton_pat_menu.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_pat_menu.setObjectName("pushButton_pat_menu")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.Patients)
        self.lineEdit_7.setGeometry(QtCore.QRect(110, 469, 741, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton = QtWidgets.QPushButton(self.Patients)
        self.pushButton.setGeometry(QtCore.QRect(860, 70, 71, 31))
        self.pushButton.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Patients)
        self.pushButton_2.setGeometry(QtCore.QRect(860, 110, 71, 31))
        self.pushButton_2.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.Patients)
        self.pushButton_3.setGeometry(QtCore.QRect(860, 150, 71, 31))
        self.pushButton_3.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 10px;\n"
"font: 10pt \\\"Segoe Print\\\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.Patients)
        self.pushButton_4.setGeometry(QtCore.QRect(860, 190, 71, 31))
        self.pushButton_4.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 10px;\n"
"font: 10pt \\\"Segoe Print\\\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.Patients)
        self.pushButton_5.setGeometry(QtCore.QRect(860, 230, 71, 31))
        self.pushButton_5.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 10px;\n"
"font: 10pt \\\"Segoe Print\\\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.Patients)
        self.pushButton_6.setGeometry(QtCore.QRect(860, 270, 71, 31))
        self.pushButton_6.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 10px;\n"
"font: 10pt \\\"Segoe Print\\\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.Patients)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 10, 41, 31))
        self.pushButton_7.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 12pt \\\"Segoe Print\\\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.Patients)
        self.pushButton_8.setGeometry(QtCore.QRect(80, 10, 41, 31))
        self.pushButton_8.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 12pt \\\"Segoe Print\\\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.Patients)
        self.pushButton_9.setGeometry(QtCore.QRect(130, 10, 41, 31))
        self.pushButton_9.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 12pt \\\"Segoe Print\\\";")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.Patients)
        self.pushButton_10.setGeometry(QtCore.QRect(180, 10, 41, 31))
        self.pushButton_10.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 12pt \\\"Segoe Print\\\";")
        self.pushButton_10.setObjectName("pushButton_10")
        self.Doctors = QtWidgets.QFrame(self.centralwidget)
        self.Doctors.setGeometry(QtCore.QRect(-10, -11, 951, 581))
        self.Doctors.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Doctors.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Doctors.setObjectName("Doctors")
        self.label_5 = QtWidgets.QLabel(self.Doctors)
        self.label_5.setGeometry(QtCore.QRect(6, 2, 951, 581))
        self.label_5.setStyleSheet("background-image: url(:/bac_image/cabinet.jpg);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.tableWidget_docotors = QtWidgets.QTableWidget(self.Doctors)
        self.tableWidget_docotors.setGeometry(QtCore.QRect(120, 81, 721, 381))
        self.tableWidget_docotors.setObjectName("tableWidget_docotors")
        self.tableWidget_docotors.setColumnCount(7)
        self.tableWidget_docotors.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_docotors.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_docotors.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_docotors.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_docotors.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_docotors.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_docotors.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_docotors.setHorizontalHeaderItem(6, item)
        self.label_6 = QtWidgets.QLabel(self.Doctors)
        self.label_6.setGeometry(QtCore.QRect(450, 40, 81, 31))
        self.label_6.setStyleSheet("font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_6.setObjectName("label_6")
        self.pushButton_doc_show = QtWidgets.QPushButton(self.Doctors)
        self.pushButton_doc_show.setGeometry(QtCore.QRect(780, 520, 111, 31))
        self.pushButton_doc_show.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_doc_show.setObjectName("pushButton_doc_show")
        self.pushButton_doc_add = QtWidgets.QPushButton(self.Doctors)
        self.pushButton_doc_add.setGeometry(QtCore.QRect(640, 520, 111, 31))
        self.pushButton_doc_add.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_doc_add.setObjectName("pushButton_doc_add")
        self.pushButton_doc_edit = QtWidgets.QPushButton(self.Doctors)
        self.pushButton_doc_edit.setGeometry(QtCore.QRect(500, 520, 111, 31))
        self.pushButton_doc_edit.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_doc_edit.setObjectName("pushButton_doc_edit")
        self.pushButton_doc_del = QtWidgets.QPushButton(self.Doctors)
        self.pushButton_doc_del.setGeometry(QtCore.QRect(360, 520, 111, 31))
        self.pushButton_doc_del.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_doc_del.setObjectName("pushButton_doc_del")
        self.pushButton_doc_search = QtWidgets.QPushButton(self.Doctors)
        self.pushButton_doc_search.setGeometry(QtCore.QRect(220, 520, 111, 31))
        self.pushButton_doc_search.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_doc_search.setObjectName("pushButton_doc_search")
        self.pushButton_doc_menu = QtWidgets.QPushButton(self.Doctors)
        self.pushButton_doc_menu.setGeometry(QtCore.QRect(80, 520, 111, 31))
        self.pushButton_doc_menu.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_doc_menu.setObjectName("pushButton_doc_menu")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.Doctors)
        self.lineEdit_15.setGeometry(QtCore.QRect(120, 470, 721, 31))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.pushButton_11 = QtWidgets.QPushButton(self.Doctors)
        self.pushButton_11.setGeometry(QtCore.QRect(860, 80, 61, 31))
        self.pushButton_11.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.Doctors)
        self.pushButton_12.setGeometry(QtCore.QRect(860, 120, 61, 31))
        self.pushButton_12.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.Doctors)
        self.pushButton_13.setGeometry(QtCore.QRect(860, 160, 61, 31))
        self.pushButton_13.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.Doctors)
        self.pushButton_14.setGeometry(QtCore.QRect(860, 200, 61, 31))
        self.pushButton_14.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.Doctors)
        self.pushButton_15.setGeometry(QtCore.QRect(30, 10, 41, 31))
        self.pushButton_15.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.Doctors)
        self.pushButton_16.setGeometry(QtCore.QRect(80, 10, 41, 31))
        self.pushButton_16.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.Doctors)
        self.pushButton_17.setGeometry(QtCore.QRect(130, 10, 41, 31))
        self.pushButton_17.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.Doctors)
        self.pushButton_18.setGeometry(QtCore.QRect(180, 10, 41, 31))
        self.pushButton_18.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_18.setObjectName("pushButton_18")
        self.Medicines = QtWidgets.QFrame(self.centralwidget)
        self.Medicines.setGeometry(QtCore.QRect(-11, -11, 961, 581))
        self.Medicines.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Medicines.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Medicines.setObjectName("Medicines")
        self.label_7 = QtWidgets.QLabel(self.Medicines)
        self.label_7.setGeometry(QtCore.QRect(6, 2, 951, 581))
        self.label_7.setStyleSheet("background-image: url(:/bac_image/cabinet.jpg);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.tableWidget_medicines = QtWidgets.QTableWidget(self.Medicines)
        self.tableWidget_medicines.setGeometry(QtCore.QRect(140, 70, 701, 381))
        self.tableWidget_medicines.setObjectName("tableWidget_medicines")
        self.tableWidget_medicines.setColumnCount(3)
        self.tableWidget_medicines.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_medicines.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_medicines.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_medicines.setHorizontalHeaderItem(2, item)
        self.pushButton_med_show = QtWidgets.QPushButton(self.Medicines)
        self.pushButton_med_show.setGeometry(QtCore.QRect(760, 520, 121, 31))
        self.pushButton_med_show.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_med_show.setObjectName("pushButton_med_show")
        self.label_8 = QtWidgets.QLabel(self.Medicines)
        self.label_8.setGeometry(QtCore.QRect(420, 30, 141, 31))
        self.label_8.setStyleSheet("font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_8.setObjectName("label_8")
        self.pushButton_med_add = QtWidgets.QPushButton(self.Medicines)
        self.pushButton_med_add.setGeometry(QtCore.QRect(620, 520, 121, 31))
        self.pushButton_med_add.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_med_add.setObjectName("pushButton_med_add")
        self.pushButton_med_edit = QtWidgets.QPushButton(self.Medicines)
        self.pushButton_med_edit.setGeometry(QtCore.QRect(480, 520, 121, 31))
        self.pushButton_med_edit.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_med_edit.setObjectName("pushButton_med_edit")
        self.pushButton_med_search = QtWidgets.QPushButton(self.Medicines)
        self.pushButton_med_search.setGeometry(QtCore.QRect(200, 520, 121, 31))
        self.pushButton_med_search.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_med_search.setObjectName("pushButton_med_search")
        self.pushButton_med_del = QtWidgets.QPushButton(self.Medicines)
        self.pushButton_med_del.setGeometry(QtCore.QRect(340, 520, 121, 31))
        self.pushButton_med_del.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_med_del.setObjectName("pushButton_med_del")
        self.pushButton_med_menu = QtWidgets.QPushButton(self.Medicines)
        self.pushButton_med_menu.setGeometry(QtCore.QRect(60, 520, 121, 31))
        self.pushButton_med_menu.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_med_menu.setObjectName("pushButton_med_menu")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.Medicines)
        self.lineEdit_21.setGeometry(QtCore.QRect(140, 470, 701, 31))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.pushButton_19 = QtWidgets.QPushButton(self.Medicines)
        self.pushButton_19.setGeometry(QtCore.QRect(850, 70, 75, 31))
        self.pushButton_19.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.Medicines)
        self.pushButton_20.setGeometry(QtCore.QRect(850, 110, 75, 31))
        self.pushButton_20.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.Medicines)
        self.pushButton_21.setGeometry(QtCore.QRect(850, 150, 75, 31))
        self.pushButton_21.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.Medicines)
        self.pushButton_22.setGeometry(QtCore.QRect(850, 190, 75, 31))
        self.pushButton_22.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.Medicines)
        self.pushButton_23.setGeometry(QtCore.QRect(40, 10, 41, 31))
        self.pushButton_23.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.Medicines)
        self.pushButton_24.setGeometry(QtCore.QRect(90, 10, 41, 31))
        self.pushButton_24.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.Medicines)
        self.pushButton_25.setGeometry(QtCore.QRect(140, 10, 41, 31))
        self.pushButton_25.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.Medicines)
        self.pushButton_26.setGeometry(QtCore.QRect(190, 10, 41, 31))
        self.pushButton_26.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_26.setObjectName("pushButton_26")
        self.Edit_patients = QtWidgets.QFrame(self.centralwidget)
        self.Edit_patients.setGeometry(QtCore.QRect(-11, -11, 951, 581))
        self.Edit_patients.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Edit_patients.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Edit_patients.setObjectName("Edit_patients")
        self.label_9 = QtWidgets.QLabel(self.Edit_patients)
        self.label_9.setGeometry(QtCore.QRect(-30, -10, 991, 601))
        self.label_9.setStyleSheet("background-image: url(:/bac_image/cabinet.jpg);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.lineEdit = QtWidgets.QLineEdit(self.Edit_patients)
        self.lineEdit.setGeometry(QtCore.QRect(372, 40, 401, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.Edit_patients)
        self.lineEdit_3.setGeometry(QtCore.QRect(370, 80, 401, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Edit_patients)
        self.lineEdit_2.setGeometry(QtCore.QRect(372, 120, 401, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.Edit_patients)
        self.lineEdit_4.setGeometry(QtCore.QRect(370, 160, 401, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_10 = QtWidgets.QLabel(self.Edit_patients)
        self.label_10.setGeometry(QtCore.QRect(156, 40, 201, 31))
        self.label_10.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.Edit_patients)
        self.label_11.setGeometry(QtCore.QRect(156, 80, 201, 31))
        self.label_11.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.Edit_patients)
        self.label_12.setGeometry(QtCore.QRect(156, 120, 201, 31))
        self.label_12.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.Edit_patients)
        self.label_13.setGeometry(QtCore.QRect(156, 160, 201, 31))
        self.label_13.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.Edit_patients)
        self.label_14.setGeometry(QtCore.QRect(156, 200, 201, 31))
        self.label_14.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.Edit_patients)
        self.label_15.setGeometry(QtCore.QRect(156, 270, 201, 31))
        self.label_15.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_15.setObjectName("label_15")
        self.pushButton_add_pat = QtWidgets.QPushButton(self.Edit_patients)
        self.pushButton_add_pat.setGeometry(QtCore.QRect(250, 510, 161, 31))
        self.pushButton_add_pat.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_add_pat.setObjectName("pushButton_add_pat")
        self.pushButton_pat_canc = QtWidgets.QPushButton(self.Edit_patients)
        self.pushButton_pat_canc.setGeometry(QtCore.QRect(570, 510, 161, 31))
        self.pushButton_pat_canc.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_pat_canc.setObjectName("pushButton_pat_canc")
        self.pushButton_edit_pat = QtWidgets.QPushButton(self.Edit_patients)
        self.pushButton_edit_pat.setGeometry(QtCore.QRect(250, 510, 161, 31))
        self.pushButton_edit_pat.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_edit_pat.setObjectName("pushButton_edit_pat")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.Edit_patients)
        self.calendarWidget.setGeometry(QtCore.QRect(370, 270, 401, 201))
        self.calendarWidget.setStyleSheet("")
        self.calendarWidget.setObjectName("calendarWidget")
        self.comboBox = QtWidgets.QComboBox(self.Edit_patients)
        self.comboBox.setGeometry(QtCore.QRect(370, 200, 401, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.Edit_medicines = QtWidgets.QFrame(self.centralwidget)
        self.Edit_medicines.setGeometry(QtCore.QRect(-10, -11, 951, 591))
        self.Edit_medicines.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Edit_medicines.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Edit_medicines.setObjectName("Edit_medicines")
        self.label_16 = QtWidgets.QLabel(self.Edit_medicines)
        self.label_16.setGeometry(QtCore.QRect(6, 2, 951, 591))
        self.label_16.setStyleSheet("background-image: url(:/bac_image/cabinet.jpg);")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.Edit_medicines)
        self.lineEdit_8.setGeometry(QtCore.QRect(380, 200, 401, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.Edit_medicines)
        self.lineEdit_9.setGeometry(QtCore.QRect(380, 260, 401, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.Edit_medicines)
        self.lineEdit_10.setGeometry(QtCore.QRect(380, 320, 401, 31))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_17 = QtWidgets.QLabel(self.Edit_medicines)
        self.label_17.setGeometry(QtCore.QRect(130, 200, 221, 31))
        self.label_17.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.Edit_medicines)
        self.label_18.setGeometry(QtCore.QRect(130, 260, 221, 31))
        self.label_18.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.Edit_medicines)
        self.label_19.setGeometry(QtCore.QRect(130, 320, 221, 31))
        self.label_19.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_19.setObjectName("label_19")
        self.pushButton_add_med = QtWidgets.QPushButton(self.Edit_medicines)
        self.pushButton_add_med.setGeometry(QtCore.QRect(310, 420, 111, 31))
        self.pushButton_add_med.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_add_med.setObjectName("pushButton_add_med")
        self.pushButton_med_canc = QtWidgets.QPushButton(self.Edit_medicines)
        self.pushButton_med_canc.setGeometry(QtCore.QRect(530, 420, 121, 31))
        self.pushButton_med_canc.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_med_canc.setObjectName("pushButton_med_canc")
        self.pushButton_edit_med = QtWidgets.QPushButton(self.Edit_medicines)
        self.pushButton_edit_med.setGeometry(QtCore.QRect(300, 420, 121, 31))
        self.pushButton_edit_med.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_edit_med.setObjectName("pushButton_edit_med")
        self.Edit_doctors = QtWidgets.QFrame(self.centralwidget)
        self.Edit_doctors.setGeometry(QtCore.QRect(-11, -1, 961, 571))
        self.Edit_doctors.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Edit_doctors.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Edit_doctors.setObjectName("Edit_doctors")
        self.label_22 = QtWidgets.QLabel(self.Edit_doctors)
        self.label_22.setGeometry(QtCore.QRect(6, -8, 951, 581))
        self.label_22.setStyleSheet("background-image: url(:/bac_image/cabinet.jpg);")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.pushButton_doc_canc = QtWidgets.QPushButton(self.Edit_doctors)
        self.pushButton_doc_canc.setGeometry(QtCore.QRect(570, 460, 121, 31))
        self.pushButton_doc_canc.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_doc_canc.setObjectName("pushButton_doc_canc")
        self.pushButton_add_doc = QtWidgets.QPushButton(self.Edit_doctors)
        self.pushButton_add_doc.setGeometry(QtCore.QRect(290, 460, 121, 31))
        self.pushButton_add_doc.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_add_doc.setObjectName("pushButton_add_doc")
        self.pushButton_edit_doc = QtWidgets.QPushButton(self.Edit_doctors)
        self.pushButton_edit_doc.setGeometry(QtCore.QRect(290, 460, 121, 31))
        self.pushButton_edit_doc.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_edit_doc.setObjectName("pushButton_edit_doc")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.Edit_doctors)
        self.lineEdit_13.setGeometry(QtCore.QRect(350, 90, 351, 31))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.Edit_doctors)
        self.lineEdit_14.setGeometry(QtCore.QRect(350, 140, 351, 31))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.Edit_doctors)
        self.lineEdit_16.setGeometry(QtCore.QRect(350, 190, 351, 31))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.Edit_doctors)
        self.lineEdit_17.setGeometry(QtCore.QRect(350, 240, 351, 31))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.Edit_doctors)
        self.lineEdit_19.setGeometry(QtCore.QRect(350, 340, 351, 31))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.Edit_doctors)
        self.lineEdit_20.setGeometry(QtCore.QRect(350, 390, 351, 31))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.label_23 = QtWidgets.QLabel(self.Edit_doctors)
        self.label_23.setGeometry(QtCore.QRect(140, 90, 191, 31))
        self.label_23.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.Edit_doctors)
        self.label_24.setGeometry(QtCore.QRect(140, 140, 191, 31))
        self.label_24.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.Edit_doctors)
        self.label_25.setGeometry(QtCore.QRect(136, 192, 191, 31))
        self.label_25.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.Edit_doctors)
        self.label_26.setGeometry(QtCore.QRect(136, 242, 191, 31))
        self.label_26.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.Edit_doctors)
        self.label_27.setGeometry(QtCore.QRect(136, 292, 191, 31))
        self.label_27.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.Edit_doctors)
        self.label_28.setGeometry(QtCore.QRect(136, 342, 191, 31))
        self.label_28.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.Edit_doctors)
        self.label_29.setGeometry(QtCore.QRect(136, 389, 191, 31))
        self.label_29.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_29.setObjectName("label_29")
        self.comboBox_2 = QtWidgets.QComboBox(self.Edit_doctors)
        self.comboBox_2.setGeometry(QtCore.QRect(350, 290, 351, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.Discount = QtWidgets.QFrame(self.centralwidget)
        self.Discount.setGeometry(QtCore.QRect(-11, -11, 961, 581))
        self.Discount.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Discount.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Discount.setObjectName("Discount")
        self.label_20 = QtWidgets.QLabel(self.Discount)
        self.label_20.setGeometry(QtCore.QRect(6, 2, 951, 581))
        self.label_20.setStyleSheet("background-image: url(:/bac_image/cabinet.jpg);")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.tableWidget_discount = QtWidgets.QTableWidget(self.Discount)
        self.tableWidget_discount.setGeometry(QtCore.QRect(150, 70, 681, 391))
        self.tableWidget_discount.setObjectName("tableWidget_discount")
        self.tableWidget_discount.setColumnCount(3)
        self.tableWidget_discount.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_discount.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_discount.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_discount.setHorizontalHeaderItem(2, item)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.Discount)
        self.lineEdit_11.setGeometry(QtCore.QRect(150, 470, 681, 31))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.pushButton_dis_add = QtWidgets.QPushButton(self.Discount)
        self.pushButton_dis_add.setGeometry(QtCore.QRect(640, 520, 131, 31))
        self.pushButton_dis_add.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_dis_add.setObjectName("pushButton_dis_add")
        self.pushButton_dis_edit = QtWidgets.QPushButton(self.Discount)
        self.pushButton_dis_edit.setGeometry(QtCore.QRect(490, 520, 131, 31))
        self.pushButton_dis_edit.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_dis_edit.setObjectName("pushButton_dis_edit")
        self.pushButton_dis_del = QtWidgets.QPushButton(self.Discount)
        self.pushButton_dis_del.setGeometry(QtCore.QRect(340, 520, 131, 31))
        self.pushButton_dis_del.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_dis_del.setObjectName("pushButton_dis_del")
        self.pushButton_dis_search = QtWidgets.QPushButton(self.Discount)
        self.pushButton_dis_search.setGeometry(QtCore.QRect(190, 520, 131, 31))
        self.pushButton_dis_search.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_dis_search.setObjectName("pushButton_dis_search")
        self.pushButton_dis_menu = QtWidgets.QPushButton(self.Discount)
        self.pushButton_dis_menu.setGeometry(QtCore.QRect(40, 520, 131, 31))
        self.pushButton_dis_menu.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_dis_menu.setObjectName("pushButton_dis_menu")
        self.pushButton_dis_show = QtWidgets.QPushButton(self.Discount)
        self.pushButton_dis_show.setGeometry(QtCore.QRect(790, 520, 131, 31))
        self.pushButton_dis_show.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_dis_show.setObjectName("pushButton_dis_show")
        self.label_21 = QtWidgets.QLabel(self.Discount)
        self.label_21.setGeometry(QtCore.QRect(440, 30, 101, 31))
        self.label_21.setStyleSheet("font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_21.setObjectName("label_21")
        self.pushButton_27 = QtWidgets.QPushButton(self.Discount)
        self.pushButton_27.setGeometry(QtCore.QRect(850, 70, 75, 31))
        self.pushButton_27.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.Discount)
        self.pushButton_28.setGeometry(QtCore.QRect(850, 110, 75, 31))
        self.pushButton_28.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtWidgets.QPushButton(self.Discount)
        self.pushButton_29.setGeometry(QtCore.QRect(850, 190, 75, 31))
        self.pushButton_29.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.Discount)
        self.pushButton_30.setGeometry(QtCore.QRect(850, 150, 75, 31))
        self.pushButton_30.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.Discount)
        self.pushButton_31.setGeometry(QtCore.QRect(50, 10, 41, 31))
        self.pushButton_31.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_32 = QtWidgets.QPushButton(self.Discount)
        self.pushButton_32.setGeometry(QtCore.QRect(100, 10, 41, 31))
        self.pushButton_32.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_33 = QtWidgets.QPushButton(self.Discount)
        self.pushButton_33.setGeometry(QtCore.QRect(150, 10, 41, 31))
        self.pushButton_33.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(self.Discount)
        self.pushButton_34.setGeometry(QtCore.QRect(200, 10, 41, 31))
        self.pushButton_34.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_34.setObjectName("pushButton_34")
        self.Edit_discount = QtWidgets.QFrame(self.centralwidget)
        self.Edit_discount.setGeometry(QtCore.QRect(-11, -11, 951, 581))
        self.Edit_discount.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Edit_discount.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Edit_discount.setObjectName("Edit_discount")
        self.label_30 = QtWidgets.QLabel(self.Edit_discount)
        self.label_30.setGeometry(QtCore.QRect(-4, 2, 961, 581))
        self.label_30.setStyleSheet("background-image: url(:/bac_image/cabinet.jpg);")
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.Edit_discount)
        self.label_31.setGeometry(QtCore.QRect(236, 200, 131, 31))
        self.label_31.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.Edit_discount)
        self.label_32.setGeometry(QtCore.QRect(236, 250, 131, 31))
        self.label_32.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.Edit_discount)
        self.label_33.setGeometry(QtCore.QRect(236, 300, 131, 31))
        self.label_33.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_33.setObjectName("label_33")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.Edit_discount)
        self.lineEdit_12.setGeometry(QtCore.QRect(390, 200, 311, 31))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.Edit_discount)
        self.lineEdit_22.setGeometry(QtCore.QRect(390, 250, 311, 31))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.Edit_discount)
        self.lineEdit_23.setGeometry(QtCore.QRect(390, 299, 311, 31))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.pushButton_add_dis = QtWidgets.QPushButton(self.Edit_discount)
        self.pushButton_add_dis.setGeometry(QtCore.QRect(274, 392, 131, 31))
        self.pushButton_add_dis.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_add_dis.setObjectName("pushButton_add_dis")
        self.pushButton_dis_canc = QtWidgets.QPushButton(self.Edit_discount)
        self.pushButton_dis_canc.setGeometry(QtCore.QRect(530, 392, 121, 31))
        self.pushButton_dis_canc.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_dis_canc.setObjectName("pushButton_dis_canc")
        self.pushButton_edit_dis = QtWidgets.QPushButton(self.Edit_discount)
        self.pushButton_edit_dis.setGeometry(QtCore.QRect(270, 390, 131, 31))
        self.pushButton_edit_dis.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_edit_dis.setObjectName("pushButton_edit_dis")
        self.Visits = QtWidgets.QFrame(self.centralwidget)
        self.Visits.setGeometry(QtCore.QRect(-11, -11, 961, 591))
        self.Visits.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Visits.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Visits.setObjectName("Visits")
        self.label_34 = QtWidgets.QLabel(self.Visits)
        self.label_34.setGeometry(QtCore.QRect(6, 2, 951, 591))
        self.label_34.setStyleSheet("background-image: url(:/bac_image/cabinet.jpg);")
        self.label_34.setText("")
        self.label_34.setObjectName("label_34")
        self.tableWidget_visits = QtWidgets.QTableWidget(self.Visits)
        self.tableWidget_visits.setGeometry(QtCore.QRect(20, 51, 691, 411))
        self.tableWidget_visits.setObjectName("tableWidget_visits")
        self.tableWidget_visits.setColumnCount(7)
        self.tableWidget_visits.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_visits.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_visits.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_visits.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_visits.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_visits.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_visits.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_visits.setHorizontalHeaderItem(6, item)
        self.pushButton_vis_show = QtWidgets.QPushButton(self.Visits)
        self.pushButton_vis_show.setGeometry(QtCore.QRect(790, 520, 131, 31))
        self.pushButton_vis_show.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_vis_show.setObjectName("pushButton_vis_show")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.Visits)
        self.lineEdit_24.setGeometry(QtCore.QRect(20, 470, 691, 31))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.pushButton_vis_add = QtWidgets.QPushButton(self.Visits)
        self.pushButton_vis_add.setGeometry(QtCore.QRect(640, 520, 131, 31))
        self.pushButton_vis_add.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_vis_add.setObjectName("pushButton_vis_add")
        self.pushButton_vis_edit = QtWidgets.QPushButton(self.Visits)
        self.pushButton_vis_edit.setGeometry(QtCore.QRect(490, 520, 131, 31))
        self.pushButton_vis_edit.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_vis_edit.setObjectName("pushButton_vis_edit")
        self.pushButton_vis_del = QtWidgets.QPushButton(self.Visits)
        self.pushButton_vis_del.setGeometry(QtCore.QRect(340, 520, 131, 31))
        self.pushButton_vis_del.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_vis_del.setObjectName("pushButton_vis_del")
        self.pushButton_vis_search = QtWidgets.QPushButton(self.Visits)
        self.pushButton_vis_search.setGeometry(QtCore.QRect(190, 520, 131, 31))
        self.pushButton_vis_search.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_vis_search.setObjectName("pushButton_vis_search")
        self.pushButton_vis_menu = QtWidgets.QPushButton(self.Visits)
        self.pushButton_vis_menu.setGeometry(QtCore.QRect(40, 520, 131, 31))
        self.pushButton_vis_menu.setStyleSheet("background-color: #FFD40D;\n"
"border-style: outset; border-width: 3px;\n"
"border-radius: 10px; border-color: #FFFF50;\n"
"font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.pushButton_vis_menu.setObjectName("pushButton_vis_menu")
        self.label_35 = QtWidgets.QLabel(self.Visits)
        self.label_35.setGeometry(QtCore.QRect(290, 10, 111, 41))
        self.label_35.setStyleSheet("font: bold 14px;\n"
"font: 14pt \\\"Segoe Print\\\";")
        self.label_35.setObjectName("label_35")
        self.tableWidget = QtWidgets.QTableWidget(self.Visits)
        self.tableWidget.setGeometry(QtCore.QRect(720, 50, 221, 131))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.Visits)
        self.tableWidget_2.setGeometry(QtCore.QRect(720, 190, 221, 141))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.Visits)
        self.tableWidget_3.setGeometry(QtCore.QRect(720, 340, 221, 161))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        self.Edit_visits.raise_()
        self.Visits.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.frame_5.raise_()
        self.frame_6.raise_()
        self.frame_7.raise_()
        self.frame_8.raise_()
        self.frame_9.raise_()
        self.Edit_medicines.raise_()
        self.Edit_doctors.raise_()
        self.Edit_patients.raise_()
        self.Patients.raise_()
        self.Medicines.raise_()
        self.Doctors.raise_()
        self.Edit_discount.raise_()
        self.Discount.raise_()
        self.Main.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_patients.setText(_translate("MainWindow", "Пацієнти"))
        self.pushButton_doctors.setText(_translate("MainWindow", "Лікарі"))
        self.pushButton_medicines.setText(_translate("MainWindow", "Прейскурант"))
        self.pushButton_visits.setText(_translate("MainWindow", "Візити"))
        self.pushButton_discount.setText(_translate("MainWindow", "Знижки"))
        self.pushButton_close.setText(_translate("MainWindow", "Вихід"))
        self.pushButton_medicines_6.setText(_translate("MainWindow", "Інфо"))
        self.label_37.setText(_translate("MainWindow", "         ID"))
        self.label_38.setText(_translate("MainWindow", "   ID пацієнта"))
        self.label_39.setText(_translate("MainWindow", "      ID лікаря"))
        self.label_40.setText(_translate("MainWindow", "Дата відвідування"))
        self.label_41.setText(_translate("MainWindow", "       Діагноз"))
        self.label_42.setText(_translate("MainWindow", "     ID знижки"))
        self.label_43.setText(_translate("MainWindow", "ID прейскуранта"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID пацієнта"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Прізвище"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID лікаря"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Прізвище"))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID знижки"))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Категорія"))
        self.pushButton_35.setText(_translate("MainWindow", "Додати"))
        self.pushButton_36.setText(_translate("MainWindow", "Скасувати"))
        self.pushButton_37.setText(_translate("MainWindow", "Змінити"))
        item = self.tableWidget_patients.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_patients.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Прізвище"))
        item = self.tableWidget_patients.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ім\'я"))
        item = self.tableWidget_patients.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "По батькові"))
        item = self.tableWidget_patients.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Стать"))
        item = self.tableWidget_patients.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Дата народження"))
        self.label_4.setText(_translate("MainWindow", "Пацієнти"))
        self.pushButton_pat_show.setText(_translate("MainWindow", "Показати"))
        self.pushButton_pat_add.setText(_translate("MainWindow", "Додати"))
        self.pushButton_pat_edit.setText(_translate("MainWindow", "Змінити"))
        self.pushButton_pat_del.setText(_translate("MainWindow", "Видалити"))
        self.pushButton_pat_search.setText(_translate("MainWindow", "Пошук"))
        self.pushButton_pat_menu.setText(_translate("MainWindow", "Меню"))
        self.pushButton.setText(_translate("MainWindow", "A"))
        self.pushButton_2.setText(_translate("MainWindow", "ID"))
        self.pushButton_3.setText(_translate("MainWindow", "Дата ↑"))
        self.pushButton_4.setText(_translate("MainWindow", "Дата ↓"))
        self.pushButton_5.setText(_translate("MainWindow", "Чол"))
        self.pushButton_6.setText(_translate("MainWindow", "Жін"))
        self.pushButton_7.setText(_translate("MainWindow", "Л"))
        self.pushButton_8.setText(_translate("MainWindow", "Пр"))
        self.pushButton_9.setText(_translate("MainWindow", "В"))
        self.pushButton_10.setText(_translate("MainWindow", "З"))
        item = self.tableWidget_docotors.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_docotors.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Прізвище"))
        item = self.tableWidget_docotors.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ім\'я"))
        item = self.tableWidget_docotors.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "По батькові"))
        item = self.tableWidget_docotors.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Спеціальність"))
        item = self.tableWidget_docotors.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Кабінет"))
        item = self.tableWidget_docotors.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Робочий телефон"))
        self.label_6.setText(_translate("MainWindow", "Лікарі"))
        self.pushButton_doc_show.setText(_translate("MainWindow", "Показати"))
        self.pushButton_doc_add.setText(_translate("MainWindow", "Додати"))
        self.pushButton_doc_edit.setText(_translate("MainWindow", "Змінити"))
        self.pushButton_doc_del.setText(_translate("MainWindow", "Видалити"))
        self.pushButton_doc_search.setText(_translate("MainWindow", "Знайти"))
        self.pushButton_doc_menu.setText(_translate("MainWindow", "Меню"))
        self.pushButton_11.setText(_translate("MainWindow", "П"))
        self.pushButton_12.setText(_translate("MainWindow", "ID"))
        self.pushButton_13.setText(_translate("MainWindow", "Каб."))
        self.pushButton_14.setText(_translate("MainWindow", "Спец."))
        self.pushButton_15.setText(_translate("MainWindow", "П"))
        self.pushButton_16.setText(_translate("MainWindow", "Пр"))
        self.pushButton_17.setText(_translate("MainWindow", "В"))
        self.pushButton_18.setText(_translate("MainWindow", "З"))
        item = self.tableWidget_medicines.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_medicines.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Вартість"))
        item = self.tableWidget_medicines.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Назва"))
        self.pushButton_med_show.setText(_translate("MainWindow", "Показати"))
        self.label_8.setText(_translate("MainWindow", "Прейскурант"))
        self.pushButton_med_add.setText(_translate("MainWindow", "Додати"))
        self.pushButton_med_edit.setText(_translate("MainWindow", "Змінити"))
        self.pushButton_med_search.setText(_translate("MainWindow", "Знайти"))
        self.pushButton_med_del.setText(_translate("MainWindow", "Видалити"))
        self.pushButton_med_menu.setText(_translate("MainWindow", "Меню"))
        self.pushButton_19.setText(_translate("MainWindow", "ID"))
        self.pushButton_20.setText(_translate("MainWindow", "↑"))
        self.pushButton_21.setText(_translate("MainWindow", "↓"))
        self.pushButton_22.setText(_translate("MainWindow", "А"))
        self.pushButton_23.setText(_translate("MainWindow", "Л"))
        self.pushButton_24.setText(_translate("MainWindow", "П"))
        self.pushButton_25.setText(_translate("MainWindow", "В"))
        self.pushButton_26.setText(_translate("MainWindow", "З"))
        self.label_10.setText(_translate("MainWindow", "          ID"))
        self.label_11.setText(_translate("MainWindow", "      Прізвище"))
        self.label_12.setText(_translate("MainWindow", "         Ім\'я"))
        self.label_13.setText(_translate("MainWindow", "    По батькові"))
        self.label_14.setText(_translate("MainWindow", "       Стать"))
        self.label_15.setText(_translate("MainWindow", "Дата народження"))
        self.pushButton_add_pat.setText(_translate("MainWindow", "Додати"))
        self.pushButton_pat_canc.setText(_translate("MainWindow", "Скасувати"))
        self.pushButton_edit_pat.setText(_translate("MainWindow", "Змінити"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Чоловіча"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Жіноча"))
        self.label_17.setText(_translate("MainWindow", "ID"))
        self.label_18.setText(_translate("MainWindow", "Вартість"))
        self.label_19.setText(_translate("MainWindow", "Назва"))
        self.pushButton_add_med.setText(_translate("MainWindow", "Додати"))
        self.pushButton_med_canc.setText(_translate("MainWindow", "Скасувати"))
        self.pushButton_edit_med.setText(_translate("MainWindow", "Змінити"))
        self.pushButton_doc_canc.setText(_translate("MainWindow", "Скасувати"))
        self.pushButton_add_doc.setText(_translate("MainWindow", "Додати"))
        self.pushButton_edit_doc.setText(_translate("MainWindow", "Змінити"))
        self.label_23.setText(_translate("MainWindow", "         ID"))
        self.label_24.setText(_translate("MainWindow", "    Прізвище"))
        self.label_25.setText(_translate("MainWindow", "        Ім\'я"))
        self.label_26.setText(_translate("MainWindow", "   По батькові"))
        self.label_27.setText(_translate("MainWindow", "  Спеціальність"))
        self.label_28.setText(_translate("MainWindow", " Номер кабінету"))
        self.label_29.setText(_translate("MainWindow", "Робочий телефон"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Лікар-стоматолог "))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Лікар-стоматолог дитячий "))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Лікар-стоматолог-ортодонт  "))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Лікар-стоматолог-ортопед "))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Лікар-стоматолог-терапевт "))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Лікар-стоматолог-хірург "))
        item = self.tableWidget_discount.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_discount.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Категорія громадян"))
        item = self.tableWidget_discount.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Знижка"))
        self.pushButton_dis_add.setText(_translate("MainWindow", "Додати"))
        self.pushButton_dis_edit.setText(_translate("MainWindow", "Змінити"))
        self.pushButton_dis_del.setText(_translate("MainWindow", "Видалити"))
        self.pushButton_dis_search.setText(_translate("MainWindow", "Знайти"))
        self.pushButton_dis_menu.setText(_translate("MainWindow", "Меню"))
        self.pushButton_dis_show.setText(_translate("MainWindow", "Показати"))
        self.label_21.setText(_translate("MainWindow", "Знижки"))
        self.pushButton_27.setText(_translate("MainWindow", "ID"))
        self.pushButton_28.setText(_translate("MainWindow", "A"))
        self.pushButton_29.setText(_translate("MainWindow", "↓"))
        self.pushButton_30.setText(_translate("MainWindow", "↑"))
        self.pushButton_31.setText(_translate("MainWindow", "П"))
        self.pushButton_32.setText(_translate("MainWindow", "Л"))
        self.pushButton_33.setText(_translate("MainWindow", "В"))
        self.pushButton_34.setText(_translate("MainWindow", "Пр"))
        self.label_31.setText(_translate("MainWindow", "ID"))
        self.label_32.setText(_translate("MainWindow", "Категорія"))
        self.label_33.setText(_translate("MainWindow", "Знижка"))
        self.pushButton_add_dis.setText(_translate("MainWindow", "Додати"))
        self.pushButton_dis_canc.setText(_translate("MainWindow", "Скасувати"))
        self.pushButton_edit_dis.setText(_translate("MainWindow", "Змінити"))
        item = self.tableWidget_visits.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Номер візиту"))
        item = self.tableWidget_visits.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID пацієнта"))
        item = self.tableWidget_visits.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ID лікаря"))
        item = self.tableWidget_visits.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Дата прийому"))
        item = self.tableWidget_visits.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Діагноз"))
        item = self.tableWidget_visits.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Знижка"))
        item = self.tableWidget_visits.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Номер рахунку"))
        self.pushButton_vis_show.setText(_translate("MainWindow", "Показати"))
        self.pushButton_vis_add.setText(_translate("MainWindow", "Додати"))
        self.pushButton_vis_edit.setText(_translate("MainWindow", "Змінити"))
        self.pushButton_vis_del.setText(_translate("MainWindow", "Видалити"))
        self.pushButton_vis_search.setText(_translate("MainWindow", "Пошук"))
        self.pushButton_vis_menu.setText(_translate("MainWindow", "Меню"))
        self.label_35.setText(_translate("MainWindow", "Візити"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID пацієнта"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Прізвище"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID лікаря"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Прізвище"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Категорія"))


