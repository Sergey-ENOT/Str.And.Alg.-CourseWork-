from classes.service import Services
from classes.tariff import Tariffs
from classes.client import Clients
from DB_interface import *
from PyQt5 import uic
import sys
import datetime


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()           # pyuic5.exe -x ..\..\DB_interface.ui -o ..\..\DB_interface.py
ui.setupUi(MainWindow)         # pyuic5.exe -x ..\..\Add_interface.ui -o ..\..\Add_interface.py
MainWindow.show()

status_edit = "not allow"

dc = Clients()
dc.import_data("csv_files/clients.csv")
# for k in dc.dict_clients.keys():
#     print(k, dc.dict_clients[k].name, dc.dict_clients[k].surname, dc.dict_clients[k].date.strftime("%d.%m.%Y"))

dc.export_data("test_file.csv")

dt = Tariffs()
dt.import_data("csv_files/tariffs.csv")


def show_table_data(dict_data, dict_t):
    ui.tableWidget.setRowCount(len(dict_data))
    ui.tableWidget.setColumnWidth(3, 125)
    ui.tableWidget.setColumnWidth(4, 250)
    row = 0
    for key in dict_data:
        dc.id_list.append(key)
        ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(dict_data[key].surname))
        ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(dict_data[key].name))
        ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(dict_data[key].patronymic))
        ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(dict_data[key].current_balance)))
        ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(dict_data[key].address))
        ui.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(datetime.datetime.strftime(dict_data[key].date, "%d.%m.%Y")))
        id_tariff = dict_data[key].ID_tariff
        obj_tariff = dict_t[str(id_tariff)]
        ui.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(obj_tariff.name))
        ui.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(dict_data[key].active))
        row += 1
    print(dc.id_list)


def print_data():
    current_row = ui.tableWidget.currentRow()
    if current_row == -1:
        pass
    else:
        obj_class = dc.dict_clients[dc.id_list[current_row]]
        ui.lineEditSurname.setText(obj_class.surname)
        ui.lineEditName.setText(obj_class.name)
        ui.lineEditPatronymic.setText(obj_class.patronymic)


def allow_edit_table():
    global status_edit
    if status_edit == "not allow":
        ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger(2))
        ui.valueStatusEdit.setText("Разрешено")
        status_edit = "allow"
    elif status_edit == "allow":
        ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger(0))
        ui.valueStatusEdit.setText("Запрещено")
        status_edit = "not allow"


# def add_data(parent):
#     new_window = uic.loadUi("Add_interface.ui")
#     new_window.setWindowTitle("New form")
#     new_window.show()
#     new_window.setParent(parent)


show_table_data(dict_data=dc.dict_clients, dict_t=dt.dict_tariffs)
ui.pushButton.clicked.connect(print_data)
ui.pushButtonEdit.clicked.connect(allow_edit_table)
#ui.pushButtonAdd.clicked.connect(add_data())

sys.exit(app.exec_())
