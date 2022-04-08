from classes.service import Services
from classes.tariff import Tariffs
from classes.client import Clients
from PyQt5 import QtCore, QtGui, QtWidgets
from DB_interface import *
import sys


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()           # pyuic5.exe -x ..\..\DB_interface.ui -o ..\..\DB_interface.py
ui.setupUi(MainWindow)
MainWindow.show()


ds = Services()
ds.import_data("csv_files/services.csv")
for k in ds.dict_services.keys():
    print(k, ds.dict_services[k])
print("------------------------")
df = Tariffs()
df.import_data("csv_files/tariffs.csv")
for k in df.dict_tariffs.keys():
    for n in df.dict_tariffs[k].services:
        df.dict_tariffs[k].price += ds.dict_services[n].price
    print(k, df.dict_tariffs[k])
print("------------------------")
dc = Clients()
dc.import_data("csv_files/clients.csv")
for k in dc.dict_clients.keys():
    print(k, dc.dict_clients[k].name, dc.dict_clients[k].surname, dc.dict_clients[k].date.strftime("%d.%m.%Y"))

dc.export_data("test_file.csv")

ui.tableWidget.setColumnWidth(0, 200)
ui.tableWidget.setColumnWidth(1, 100)
ui.load_data()


sys.exit(app.exec_())
