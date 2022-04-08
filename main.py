from classes.service import Services
from classes.tariff import Tariffs
from classes.client import Clients
from DB_interface import *
import sys


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()           # pyuic5.exe -x ..\..\DB_interface.ui -o ..\..\DB_interface.py
ui.setupUi(MainWindow)
MainWindow.show()


dc = Clients()
dc.import_data("csv_files/clients.csv")
# for k in dc.dict_clients.keys():
#     print(k, dc.dict_clients[k].name, dc.dict_clients[k].surname, dc.dict_clients[k].date.strftime("%d.%m.%Y"))

dc.export_data("test_file.csv")


def show_table_data(dict_data):
    ui.tableWidget.setRowCount(len(dict_data))
    ui.tableWidget.setColumnCount(8)
    ui.tableWidget.setColumnWidth(4, 250)
    ui.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("name"))
    ui.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("surname"))
    ui.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("patronymic"))
    ui.tableWidget.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("current balance"))
    ui.tableWidget.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem("address"))
    ui.tableWidget.setHorizontalHeaderItem(5, QtWidgets.QTableWidgetItem("date"))
    ui.tableWidget.setHorizontalHeaderItem(6, QtWidgets.QTableWidgetItem("ID_tariff"))
    ui.tableWidget.setHorizontalHeaderItem(7, QtWidgets.QTableWidgetItem("active"))
    row = 0
    for key in dict_data:
        ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(dict_data[key].name))
        ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(dict_data[key].surname))
        ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(dict_data[key].patronymic))
        ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(dict_data[key].current_balance)))
        ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(dict_data[key].address))
        ui.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(dict_data[key].date)))
        ui.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(dict_data[key].ID_tariff))
        ui.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(dict_data[key].active))
        row += 1


def print_data():
    for i in range(ui.tableWidget.rowCount()):
        for j in range(ui.tableWidget.columnCount()):
            print(ui.tableWidget.item(i, j).text(), end=" ")
        print("\n---------------")


show_table_data(dict_data=dc.dict_clients)
ui.pushButton.clicked.connect(print_data)
sys.exit(app.exec_())
