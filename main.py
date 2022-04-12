from classes.service import Services
from classes.tariff import Tariffs
from classes.client import Clients, Client
from DB_interface import *
import sys
import datetime
import traceback

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()  # pyuic5.exe -x ..\..\DB_interface.ui -o ..\..\DB_interface.py
ui.setupUi(MainWindow)
MainWindow.show()

status_edit = "not allow"
list_taken_id = []

dc = Clients()
dc.import_data("csv_files/Clients.csv")

dt = Tariffs()
dt.import_data("csv_files/Tariffs.csv")


def log_uncaught_exceptions(ex_cls, ex, tb): # error catcher
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    text += ''.join(traceback.format_tb(tb))
    print(text)
    QtWidgets.QMessageBox.critical(None, 'Error', text)
    sys.exit()


sys.excepthook = log_uncaught_exceptions


def show_table_data(dict_data, dict_t, dict_index):
    global list_taken_id
    ui.tableWidget.setRowCount(len(dict_data))
    ui.tableWidget.setColumnWidth(3, 125)
    ui.tableWidget.setColumnWidth(4, 250)
    row = 0
    for key in dict_data:
        dc.id_list_pos.append(key)
        ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(dict_data[key].surname))
        ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(dict_data[key].name))
        ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(dict_data[key].patronymic))
        ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(dict_data[key].current_balance)))
        ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(dict_data[key].address))
        ui.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(dict_data[key].date))
        id_tariff = dict_data[key].ID_tariff
        obj_tariff = dict_t[str(id_tariff)]
        ui.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(obj_tariff.name))
        ui.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(dict_data[key].active))
        list_taken_id.append(key)
        row += 1
    for key in dict_t.keys():
        ui.comboBoxTariff.addItem(str(dict_t[key].name))
    ui.comboBoxActive.addItem("1")
    ui.comboBoxActive.addItem("0")
    for key in dict_t:
        dict_index[dict_t[key].name] = key


def print_data():
    current_row = ui.tableWidget.currentRow()
    if current_row == -1:
        pass
    else:
        obj_class = dc.dict_clients[dc.id_list_pos[current_row]]
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


def add_data():
    global list_taken_id
    new_id = ""
    count = 0
    g_surname = ui.lineEditSurname.text()
    g_name = ui.lineEditName.text()
    g_patronymic = ui.lineEditPatronymic.text()
    g_current_b = ui.lineEditCurrentB.text()
    g_address = ui.lineEditAddress.text()
    g_date = ui.lineEditDate.text()
    g_tariff = ui.comboBoxTariff.currentText()
    g_tariff_id = dt.id_dict_tariff[g_tariff]
    g_active = ui.comboBoxActive.currentText()

    set_taken_id = set(list_taken_id)
    for i in range(len(list_taken_id)):
        count = i + 1
        if str(count) not in set_taken_id:
            new_id = count
            break
        elif i == (len(list_taken_id) - 1):
            new_id = int(list_taken_id[i]) + 1
    dc.dict_clients[new_id] = Client(g_surname, g_name, g_patronymic, g_current_b,
                                     g_address, g_date, g_tariff_id, g_active)
    dc.export_data("csv_files/Clients.csv")
    dc.dict_clients = {}
    list_taken_id = []
    dt.id_dict_tariff = {}
    dc.import_data("csv_files/Clients.csv")
    show_table_data(dict_data=dc.dict_clients, dict_t=dt.dict_tariffs, dict_index=dt.id_dict_tariff)


show_table_data(dict_data=dc.dict_clients, dict_t=dt.dict_tariffs, dict_index=dt.id_dict_tariff)
ui.pushButton.clicked.connect(print_data)
ui.pushButtonEdit.clicked.connect(allow_edit_table)
ui.pushButtonAdd.clicked.connect(add_data)

sys.exit(app.exec_())
