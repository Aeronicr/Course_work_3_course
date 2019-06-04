import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3
import design
import resource
import Database_module


SQL_INSERT_PATIENTS = "INSERT INTO patients (surname, name, last_name, sex, date_birth) VALUES (?, ?, ?, ?, ?)"
SQL_UPDATE_PATIENTS = "UPDATE patients SET surname = ?, name = ?, last_name = ?, sex = ?, date_birth = ? WHERE id_patient = ?"
SQL_DELETE_PATIENTS = "DELETE from patients WHERE id_patient=?"
SQL_INSERT_DOCTORS = "INSERT INTO doctors (surname, name, last_name, specialty, cabinet_number, work_phone) VALUES (?, ?, ?, ?, ?, ?)"
SQL_UPDATE_DOCTORS = "UPDATE doctors SET surname = ?, name = ?, last_name = ?, specialty = ?, cabinet_number = ?, work_phone = ? WHERE id_doctor = ?"
SQL_DELETE_DOCTORS = "DELETE from doctors WHERE id_doctor=?"
SQL_INSERT_MEDICINES = "INSERT INTO price_list (title, cost_service) VALUES (?, ?)"
SQL_UPDATE_MEDICINES = "UPDATE price_list SET title = ?, cost_service = ? WHERE destination_code = ?"
SQL_DELETE_MEDICINES = "DELETE from price_list WHERE destination_code=?"
SQL_INSERT_DISCOUNT = "INSERT INTO discount (categories_citizen, interest_discount) VALUES (?, ?)"
SQL_UPDATE_DISCOUNT = "UPDATE discount SET interest_discount = ?, categories_citizen = ? WHERE discount_code = ?"
SQL_DELETE_DISCOUNT = "DELETE from discount WHERE discount_code=?"
SQL_SORT_DOCTORS = "SELECT * FROM doctors ORDER BY cabinet_number =?"
SQL_INSERT_VISITS = "INSERT INTO appeals (id_patient, id_doctor, date_application, diagnosis, discount_code, destination_code) VALUES (?, ?, ?, ?, ?, ?)"


class Main(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.creation()

    def creation(self):
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle("Програмний модуль автоматизації роботи платної стоматологічної поліклініки")
        self.setWindowIcon(QIcon('images/icon1.jpg'))
        self.Main.show()
        self.Patients.hide()
        self.pushButton_patients.clicked.connect(self.database_patients)
        self.pushButton_doctors.clicked.connect(self.database_doctors)
        self.pushButton_medicines.clicked.connect(self.database_medicines)
        self.pushButton_discount.clicked.connect(self.database_discount)
        self.pushButton_visits.clicked.connect(self.database_visits)
        self.pushButton_close.clicked.connect(sys.exit)

    def database_patients(self):
        self.Main.hide()
        self.Edit_doctors.hide()
        self.Doctors.hide()
        self.Edit_patients.hide()
        self.Patients.show()
        self.Edit_discount.hide()
        self.Medicines.hide()
        self.Discount.hide()
        self.Edit_medicines.hide()
        self.pushButton_pat_show.clicked.connect(self.load_patients)
        self.pushButton_pat_add.clicked.connect(self.add_patients)
        self.pushButton_pat_edit.clicked.connect(self.edit_patients)
        self.pushButton_pat_del.clicked.connect(self.delete_patients)
        self.pushButton_pat_search.clicked.connect(self.search_patients)
        self.pushButton_pat_menu.clicked.connect(self.creation)
        self.pushButton.clicked.connect(self.sort_alpha_patients)
        self.pushButton_2.clicked.connect(self.sort_id_patients)
        self.pushButton_3.clicked.connect(self.sort_date_patients)
        self.pushButton_4.clicked.connect(self.sort_date2_patients)
        self.pushButton_5.clicked.connect(self.sort_sex1_patients)
        self.pushButton_6.clicked.connect(self.sort_sex2_patients)
        self.pushButton_7.clicked.connect(self.database_doctors)
        self.pushButton_8.clicked.connect(self.database_medicines)
        self.pushButton_9.clicked.connect(self.database_visits)
        self.pushButton_10.clicked.connect(self.database_discount)
        self.tableWidget_patients.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.read_from_db_pat()):
            self.tableWidget_patients.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_patients.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def load_patients(self):
        self.lineEdit_7.clear()
        self.tableWidget_patients.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.read_from_db_pat()):
            self.tableWidget_patients.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_patients.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def add_patients(self):
        self.Main.hide()
        self.Patients.hide()
        self.Doctors.hide()
        self.Medicines.hide()
        self.Edit_medicines.hide()
        self.Edit_doctors.hide()
        self.pushButton_edit_pat.hide()
        self.lineEdit.hide()
        self.label_10.hide()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.Edit_patients.show()
        self.pushButton_add_pat.show()
        self.pushButton_add_pat.clicked.connect(self.add_patients2)
        self.pushButton_pat_canc.clicked.connect(self.database_patients)

    def add_patients2(self):
        surname = self.lineEdit_3.text()
        name = self.lineEdit_2.text()
        last_name = self.lineEdit_4.text()
        sex = self.comboBox.currentText()
        date = self.calendarWidget.selectedDate()
        date_birth = date.toString(("dd.MM.yyyy"))
        connection = sqlite3.connect('Dental_clinic.db')
        curs = connection.cursor()
        curs.execute(SQL_INSERT_PATIENTS,(surname, name, last_name, sex, date_birth))
        connection.commit()
        connection.close()
        self.Edit_patients.hide()
        self.Edit_doctors.hide()
        self.Edit_medicines.hide()
        self.Doctors.hide()
        self.Medicines.hide()
        self.Patients.show()

    def edit_patients(self):
        self.Main.hide()
        self.Doctors.hide()
        self.Medicines.hide()
        self.Patients.hide()
        self.Edit_doctors.hide()
        self.Edit_medicines.hide()
        self.pushButton_edit_pat.hide()
        self.lineEdit.show()
        self.label_10.show()
        self.pushButton_add_pat.hide()
        self.pushButton_edit_pat.show()
        self.lineEdit.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_2.clear()
        self.Edit_patients.show()
        self.pushButton_edit_pat.clicked.connect(self.edit_patients2)
        self.pushButton_pat_canc.clicked.connect(self.database_patients)

    def edit_patients2(self):
        id_patient = self.lineEdit.text()
        surname = self.lineEdit_3.text()
        name = self.lineEdit_2.text()
        last_name = self.lineEdit_4.text()
        sex = self.comboBox.currentText()
        date = self.calendarWidget.selectedDate()
        date_birth = date.toString(("dd.MM.yyyy"))
        connection = sqlite3.connect('Dental_clinic.db')
        curs = connection.cursor()
        curs.execute(SQL_UPDATE_PATIENTS,(surname, name, last_name, sex, date_birth, id_patient))
        connection.commit()
        connection.close()
        self.Edit_patients.hide()
        self.Edit_medicines.hide()
        self.Doctors.hide()
        self.Patients.show()

    def delete_patients(self):
        self.Main.hide()
        self.Medicines.hide()
        self.Edit_patients.hide()
        self.Edit_medicines.hide()
        self.Edit_doctors.hide()
        self.Patients.show()
        text = self.lineEdit_7.text()
        connection = sqlite3.connect('Dental_clinic.db')
        curs = connection.cursor()
        curs.execute(SQL_DELETE_PATIENTS, (text,))
        connection.commit()
        connection.close()

    def search_patients(self):
        text = self.lineEdit_7.text()
        rows = self.tableWidget_patients.rowCount()
        cols = self.tableWidget_patients.columnCount()
        first = None
        for i in range(rows):
            for j in range(cols):
                txt = self.tableWidget_patients.item(i, j).text()
                if text in txt:
                    self.tableWidget_patients.item(i, j)
                    if not first: first = self.tableWidget_patients.item(i, j)
        self.tableWidget_patients.setCurrentItem(first)
        self.lineEdit_7.clear()

    def sort_alpha_patients(self):
        self.tableWidget_patients.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.sort_alpha_pat()):
            self.tableWidget_patients.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_patients.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def sort_id_patients(self):
        self.tableWidget_patients.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.sort_id_pat()):
            self.tableWidget_patients.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_patients.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def sort_date_patients(self):
        self.tableWidget_patients.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.sort_date_pat()):
            self.tableWidget_patients.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_patients.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def sort_date2_patients(self):
        self.tableWidget_patients.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.sort_date_pat_down()):
            self.tableWidget_patients.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_patients.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def sort_sex1_patients(self):
        self.tableWidget_patients.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.sort_sex1_pat()):
            self.tableWidget_patients.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_patients.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def sort_sex2_patients(self):
        self.tableWidget_patients.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.sort_sex2_pat()):
            self.tableWidget_patients.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_patients.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

#####################################################################################
    # Doctors
#####################################################################################

    def database_doctors(self):
        self.Main.hide()
        self.Edit_doctors.hide()
        self.Edit_patients.hide()
        self.Edit_medicines.hide()
        self.Patients.hide()
        self.Doctors.show()
        self.Medicines.hide()
        self.Edit_discount.hide()
        self.Discount.hide()
        self.pushButton_doc_show.clicked.connect(self.load_doctors)
        self.pushButton_doc_add.clicked.connect(self.add_doctors)
        self.pushButton_doc_edit.clicked.connect(self.edit_doctors)
        self.pushButton_doc_del.clicked.connect(self.delete_doctors)
        self.pushButton_doc_search.clicked.connect(self.search_doctors)
        self.pushButton_doc_menu.clicked.connect(self.creation)
        self.pushButton_15.clicked.connect(self.database_patients)
        self.pushButton_16.clicked.connect(self.database_medicines)
        self.pushButton_17.clicked.connect(self.database_visits)
        self.pushButton_18.clicked.connect(self.database_discount)
        self.pushButton_11.clicked.connect(self.sort_alpha_doctors)
        self.pushButton_12.clicked.connect(self.sort_id_doctors)
        self.pushButton_13.clicked.connect(self.sort_cab_doctors)
        self.pushButton_14.clicked.connect(self.sort_spec_doctors)
        self.tableWidget_docotors.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.read_from_db_doc()):
            self.tableWidget_docotors.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_docotors.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def load_doctors(self):
        self.tableWidget_docotors.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.read_from_db_doc()):
            self.tableWidget_docotors.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_docotors.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def add_doctors(self):
        self.Main.hide()
        self.Patients.hide()
        self.Medicines.hide()
        self.Doctors.hide()
        self.Edit_doctors.show()
        self.Edit_medicines.hide()
        self.pushButton_edit_doc.hide()
        self.lineEdit_13.hide()
        self.label_23.hide()
        self.pushButton_add_doc.show()
        self.pushButton_add_doc.clicked.connect(self.add_doctors2)
        self.pushButton_doc_canc.clicked.connect(self.database_doctors)

    def add_doctors2(self):
        surname = self.lineEdit_14.text()
        name = self.lineEdit_16.text()
        last_name = self.lineEdit_17.text()
        specialty = self.comboBox_2.currentText()
        cabinet_number = self.lineEdit_19.text()
        work_phone = self.lineEdit_20.text()
        connection = sqlite3.connect('Dental_clinic.db')
        curs = connection.cursor()
        curs.execute(SQL_INSERT_DOCTORS,(surname, name, last_name, specialty, cabinet_number, work_phone))
        connection.commit()
        connection.close()
        self.Edit_patients.hide()
        self.Edit_medicines.hide()
        self.Edit_doctors.hide()
        self.Doctors.show()
        self.Patients.hide()
        self.Medicines.hide()

    def edit_doctors(self):
        self.Main.hide()
        self.Patients.hide()
        self.Doctors.hide()
        self.Medicines.hide()
        self.Edit_medicines.hide()
        self.Edit_doctors.show()
        self.pushButton_edit_doc.show()
        self.lineEdit_13.show()
        self.label_23.show()
        self.pushButton_add_doc.hide()
        self.pushButton_edit_doc.clicked.connect(self.edit_doctors2)
        self.pushButton_doc_canc.clicked.connect(self.database_doctors)

    def edit_doctors2(self):
        id_doctor = self.lineEdit_13.text()
        surname = self.lineEdit_14.text()
        name = self.lineEdit_16.text()
        last_name = self.lineEdit_17.text()
        specialty = self.comboBox_2.currentText()
        cabinet_number = self.lineEdit_19.text()
        work_phone = self.lineEdit_20.text()
        connection = sqlite3.connect('Dental_clinic.db')
        curs = connection.cursor()
        curs.execute(SQL_UPDATE_DOCTORS,(surname, name, last_name, specialty, cabinet_number, work_phone, id_doctor))
        connection.commit()
        connection.close()
        self.Edit_patients.hide()
        self.Edit_doctors.hide()
        self.Edit_medicines.hide()
        self.Doctors.show()
        self.Medicines.hide()
        self.Patients.hide()

    def delete_doctors(self):
        self.Main.hide()
        self.Edit_patients.hide()
        self.Edit_doctors.hide()
        self.Edit_medicines.hide()
        self.Medicines.hide()
        self.Patients.hide()
        self.Doctors.show()
        text = self.lineEdit_15.text()
        connection = sqlite3.connect('Dental_clinic.db')
        curs = connection.cursor()
        curs.execute(SQL_DELETE_DOCTORS, (text,))
        connection.commit()
        connection.close()

    def search_doctors(self):
        text = self.lineEdit_15.text()
        rows = self.tableWidget_docotors.rowCount()
        cols = self.tableWidget_docotors.columnCount()
        first = None
        for i in range(rows):
            for j in range(cols):
                txt = self.tableWidget_docotors.item(i, j).text()
                if text in txt:
                    self.tableWidget_docotors.item(i, j)
                    if not first: first = self.tableWidget_docotors.item(i, j)
        self.tableWidget_docotors.setCurrentItem(first)

    def sort_alpha_doctors(self):
        self.tableWidget_docotors.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.sort_alpha_doc()):
            self.tableWidget_docotors.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_docotors.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


    def sort_id_doctors(self):
        self.tableWidget_docotors.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.sort_id_doc()):
            self.tableWidget_docotors.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_docotors.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def sort_cab_doctors(self):
        self.tableWidget_docotors.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.sort_id_cab()):
            self.tableWidget_docotors.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_docotors.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def sort_spec_doctors(self):
        self.tableWidget_docotors.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.sort_id_spec()):
            self.tableWidget_docotors.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_docotors.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


####################################################################################
    #Medicines
####################################################################################
    def database_medicines(self):
        self.Main.hide()
        self.Edit_doctors.hide()
        self.Edit_patients.hide()
        self.Edit_medicines.hide()
        self.Patients.hide()
        self.Discount.hide()
        self.Edit_discount.hide()
        self.Doctors.hide()
        self.Medicines.show()
        self.pushButton_med_show.clicked.connect(self.load_medicines)
        self.pushButton_med_add.clicked.connect(self.add_medicines)
        self.pushButton_med_edit.clicked.connect(self.edit_medicines)
        self.pushButton_med_del.clicked.connect(self.delete_medicines)
        self.pushButton_med_search.clicked.connect(self.search_medicines)
        self.pushButton_med_menu.clicked.connect(self.creation)
        self.pushButton_22.clicked.connect(self.sort_alpha_medicines)
        self.pushButton_19.clicked.connect(self.sort_id_medicines)
        self.pushButton_20.clicked.connect(self.sort_cost1_medicines)
        self.pushButton_21.clicked.connect(self.sort_cost2_medicines)
        self.pushButton_24.clicked.connect(self.database_patients)
        self.pushButton_23.clicked.connect(self.database_doctors)
        self.pushButton_25.clicked.connect(self.database_visits)
        self.pushButton_26.clicked.connect(self.database_discount)
        self.tableWidget_medicines.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.read_from_db_med()):
            self.tableWidget_medicines.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_medicines.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def load_medicines(self):
        self.tableWidget_medicines.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.read_from_db_med()):
            self.tableWidget_medicines.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_medicines.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def add_medicines(self):
        self.Main.hide()
        self.Patients.hide()
        self.Medicines.hide()
        self.Doctors.hide()
        self.Edit_medicines.show()
        self.Edit_doctors.hide()
        self.pushButton_edit_med.hide()
        self.lineEdit_8.hide()
        self.label_17.hide()
        self.pushButton_add_med.show()
        self.pushButton_add_med.clicked.connect(self.add_medicines2)
        self.pushButton_med_canc.clicked.connect(self.database_medicines)

    def add_medicines2(self):
        title = self.lineEdit_10.text()
        cost_service = self.lineEdit_9.text()
        connection = sqlite3.connect('Dental_clinic.db')
        curs = connection.cursor()
        curs.execute(SQL_INSERT_MEDICINES,(title, cost_service))
        connection.commit()
        connection.close()
        self.Edit_patients.hide()
        self.Edit_doctors.hide()
        self.Edit_medicines.hide()
        self.Doctors.hide()
        self.Patients.hide()
        self.Medicines.show()

    def edit_medicines(self):
        self.Main.hide()
        self.Patients.hide()
        self.Medicines.hide()
        self.Edit_doctors.hide()
        self.Doctors.hide()
        self.Edit_medicines.show()
        self.pushButton_edit_med.show()
        self.lineEdit_8.show()
        self.label_17.show()
        self.pushButton_add_med.hide()
        self.pushButton_edit_med.clicked.connect(self.edit_medicines2)
        self.pushButton_med_canc.clicked.connect(self.database_medicines)

    def edit_medicines2(self):
        destination_code = self.lineEdit_8.text()
        title = self.lineEdit_10.text()
        cost = self.lineEdit_9.text()
        connection = sqlite3.connect('Dental_clinic.db')
        curs = connection.cursor()
        curs.execute(SQL_UPDATE_MEDICINES,(title, cost, destination_code))
        connection.commit()
        connection.close()
        self.Edit_patients.hide()
        self.Edit_doctors.hide()
        self.Edit_medicines.hide()
        self.Medicines.show()
        self.Doctors.hide()
        self.Patients.hide()

    def delete_medicines(self):
        self.Main.hide()
        self.Edit_patients.hide()
        self.Edit_doctors.hide()
        self.Edit_medicines.hide()
        self.Medicines.show()
        self.Patients.hide()
        self.Doctors.hide()
        text = self.lineEdit_21.text()
        connection = sqlite3.connect('Dental_clinic.db')
        curs = connection.cursor()
        curs.execute(SQL_DELETE_MEDICINES, (text,))
        connection.commit()
        connection.close()

    def search_medicines(self):
        text = self.lineEdit_21.text()
        rows = self.tableWidget_medicines.rowCount()
        cols = self.tableWidget_medicines.columnCount()
        first = None
        for i in range(rows):
            for j in range(cols):
                txt = self.tableWidget_medicines.item(i, j).text()
                if text in txt:
                    self.tableWidget_medicines.item(i, j)
                    if not first: first = self.tableWidget_medicines.item(i, j)
        self.tableWidget_medicines.setCurrentItem(first)

    def sort_alpha_medicines(self):
        self.tableWidget_docotors.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.sort_alpha_doc()):
            self.tableWidget_docotors.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_docotors.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def sort_id_medicines(self):
        self.tableWidget_docotors.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.sort_id_medicines()):
            self.tableWidget_docotors.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_docotors.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def sort_cost1_medicines(self):
        self.tableWidget_docotors.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.sort_cost1_medicines()):
            self.tableWidget_docotors.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_docotors.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def sort_cost2_medicines(self):
        self.tableWidget_docotors.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.sort_cost2_medicines()):
            self.tableWidget_docotors.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_docotors.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

#############################################################################
    #Discount
#############################################################################

    def database_discount(self):
        self.Main.hide()
        self.Edit_doctors.hide()
        self.Edit_patients.hide()
        self.Edit_medicines.hide()
        self.Patients.hide()
        self.Doctors.hide()
        self.Medicines.hide()
        self.Discount.show()
        self.pushButton_dis_show.clicked.connect(self.load_discount)
        self.pushButton_dis_add.clicked.connect(self.add_discount)
        self.pushButton_dis_edit.clicked.connect(self.edit_discount)
        self.pushButton_dis_del.clicked.connect(self.delete_discount)
        self.pushButton_dis_search.clicked.connect(self.search_discount)
        self.pushButton_dis_menu.clicked.connect(self.creation)
        self.pushButton_27.clicked.connect(self.sort_id_discount)
        self.pushButton_28.clicked.connect(self.sort_id_alpha)
        self.pushButton_30.clicked.connect(self.sort_interest1_dis)
        self.pushButton_29.clicked.connect(self.sort_interest2_dis)
        self.pushButton_31.clicked.connect(self.database_patients)
        self.pushButton_32.clicked.connect(self.database_doctors)
        self.pushButton_33.clicked.connect(self.database_visits)
        self.pushButton_34.clicked.connect(self.database_medicines)
        self.tableWidget_discount.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.read_from_db_dis()):
            self.tableWidget_discount.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_discount.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def load_discount(self):
        self.tableWidget_discount.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.read_from_db_dis()):
            self.tableWidget_discount.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_discount.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def add_discount(self):
        self.Main.hide()
        self.Patients.hide()
        self.Medicines.hide()
        self.Doctors.hide()
        self.Discount.hide()
        self.Edit_medicines.hide()
        self.Edit_discount.show()
        self.Edit_doctors.hide()
        self.pushButton_edit_med.hide()
        self.lineEdit_12.hide()
        self.label_31.hide()
        self.pushButton_add_dis.show()
        self.pushButton_edit_dis.hide()
        self.pushButton_add_dis.clicked.connect(self.add_discount2)
        self.pushButton_dis_canc.clicked.connect(self.database_discount)

    def add_discount2(self):
        categories_citizen = self.lineEdit_22.text()
        interest_discount = self.lineEdit_23.text()
        connection = sqlite3.connect('Dental_clinic.db')
        curs = connection.cursor()
        curs.execute(SQL_INSERT_DISCOUNT,(categories_citizen, interest_discount))
        connection.commit()
        connection.close()
        self.Edit_patients.hide()
        self.Edit_doctors.hide()
        self.Edit_medicines.hide()
        self.Edit_discount.show()
        self.Medicines.hide()
        self.Discount.show()
        self.Doctors.hide()
        self.Patients.hide()

    def edit_discount(self):
        self.Main.hide()
        self.Patients.hide()
        self.Medicines.hide()
        self.Discount.hide()
        self.Edit_doctors.hide()
        self.Doctors.hide()
        self.Edit_medicines.hide()
        self.Edit_discount.show()
        self.pushButton_edit_dis.show()
        self.lineEdit_12.show()
        self.label_31.show()
        self.pushButton_add_dis.hide()
        self.pushButton_edit_dis.clicked.connect(self.edit_discount2)
        self.pushButton_dis_canc.clicked.connect(self.database_discount)

    def edit_discount2(self):
        discount_code = self.lineEdit_12.text()
        categories_citizen = self.lineEdit_22.text()
        interest_discount = self.lineEdit_23.text()
        curs = connection.cursor()
        connection = sqlite3.connect('Dental_clinic.db')
        curs.execute(SQL_UPDATE_DISCOUNT,(interest_discount, categories_citizen, discount_code))
        connection.commit()
        connection.close()
        self.Edit_patients.hide()
        self.Edit_doctors.hide()
        self.Edit_medicines.hide()
        self.Medicines.hide()
        self.Discount.show()
        self.Doctors.hide()
        self.Patients.hide()

    def delete_discount(self):
        text = self.lineEdit_11.text()
        connection = sqlite3.connect('Dental_clinic.db')
        curs = connection.cursor()
        curs.execute(SQL_DELETE_DISCOUNT, (text,))
        connection.commit()
        connection.close()

    def search_discount(self):
        text = self.lineEdit_11.text()
        rows = self.tableWidget_discount.rowCount()
        cols = self.tableWidget_discount.columnCount()
        first = None
        for i in range(rows):
            for j in range(cols):
                txt = self.tableWidget_discount.item(i, j).text()
                if text in txt:
                    self.tableWidget_discount.item(i, j)
                    if not first: first = self.tableWidget_discount.item(i, j)
        self.tableWidget_discount.setCurrentItem(first)

    def sort_id_discount(self):
        self.tableWidget_discount.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.sort_id_dis()):
            self.tableWidget_discount.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_discount.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def sort_id_alpha(self):
        self.tableWidget_discount.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.sort_id_alpha()):
            self.tableWidget_discount.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_discount.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def sort_interest1_dis(self):
        self.tableWidget_discount.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.sort_interest1_dis()):
            self.tableWidget_discount.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_discount.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def sort_interest2_dis(self):
        self.tableWidget_discount.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.sort_interest2_dis()):
            self.tableWidget_discount.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_discount.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

##############################################################################
    #Visits
##############################################################################

    def database_visits(self):
        self.Visits.show()
        self.Main.hide()
        self.Edit_doctors.hide()
        self.Edit_discount.hide()
        self.Edit_patients.hide()
        self.Edit_medicines.hide()
        self.Edit_discount.hide()
        self.Patients.hide()
        self.Doctors.hide()
        self.Medicines.hide()
        self.Discount.hide()
        self.Visits.show()
        self.pushButton_vis_show.clicked.connect(self.load_visits)
        self.pushButton_vis_add.clicked.connect(self.add_visits)
        # self.pushButton_vis_edit.clicked.connect(self.edit_discount)
        # self.pushButton_vis_del.clicked.connect(self.delete_discount)
        # self.pushButton_vis_search.clicked.connect(self.search_discount)
        # self.pushButton_vis_menu.clicked.connect(self.creation)
        self.tableWidget_visits.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.read_from_db_vis()):
            self.tableWidget_visits.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_visits.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.read_vis_pat()):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        self.tableWidget_2.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.read_vis_doc()):
            self.tableWidget_2.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        self.tableWidget_3.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.read_vis_dis()):
            self.tableWidget_3.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_3.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def load_visits(self):
        self.tableWidget_visits.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.read_from_db_vis()):
            self.tableWidget_visits.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_visits.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def add_visits(self):
        self.Main.hide()
        self.Visits.hide()
        self.Patients.hide()
        self.Medicines.hide()
        self.Doctors.hide()
        self.Discount.hide()
        self.Edit_medicines.hide()
        self.Edit_discount.hide()
        self.Edit_doctors.hide()
        self.Edit_visits.show()
        self.lineEdit_5.hide()
        self.label_37.hide()
        self.pushButton_37.hide()
        self.pushButton_35.clicked.connect(self.add_visits2)
        self.pushButton_36.clicked.connect(self.database_visits)
        self.tableWidget_4.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.read_vis_pat()):
            self.tableWidget_4.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_4.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        self.tableWidget_5.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.read_vis_doc()):
            self.tableWidget_5.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_5.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        self.tableWidget_6.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.read_vis_dis()):
            self.tableWidget_6.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_6.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def load_visits(self):
        self.tableWidget_6.setRowCount(0)
        for row_number, row_data in enumerate(Database_module.read_from_db_vis()):
            self.tableWidget_6.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_6.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def add_visits2(self):
        id_patient = self.lineEdit_6.text()
        id_doctor = self.lineEdit_18.text()
        diagnosis = self.lineEdit_26.text()
        discount_code = self.lineEdit_27.text()
        destination_code = self.lineEdit_28.text()
        date = self.calendarWidget_2.selectedDate()
        date_application = date.toString(("dd.MM.yyyy"))
        connection = sqlite3.connect('Dental_clinic.db', timeout=10)
        curs = connection.cursor()
        curs.execute(SQL_INSERT_VISITS, (id_patient, id_doctor, diagnosis, discount_code, destination_code, date_application))
        connection.commit()
        connection.close()
        self.Edit_patients.hide()

        self.Edit_doctors.hide()
        self.Edit_medicines.hide()
        self.Edit_discount.hide()
        self.Edit_visits.hide()
        self.Medicines.hide()
        self.Discount.hide()
        self.Doctors.hide()
        self.Visits.show()
        self.Patients.hide()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())