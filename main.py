from classes.service import Services
from classes.tariff import Tariffs
from classes.client import Clients, Client
from DB_interface import *
from PyQt5.QtWidgets import QMessageBox
import sys
from datetime import datetime
import traceback


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()  # pyuic5.exe -x ..\..\DB_interface.ui -o ..\..\DB_interface.py
ui.setupUi(MainWindow)
MainWindow.show()

ui.tableWidget.setColumnWidth(3, 125)
ui.tableWidget.setColumnWidth(4, 300)
ui.tableWidget.setColumnWidth(7, 70)
ui.tableWidgetTariff.setColumnWidth(1, 400)
ui.tableWidgetService.setColumnWidth(0, 200)
ui.tableWidgetService.setColumnWidth(1, 125)
ui.pushButtonChooseClient.setText("Выбрать\nзапись")
ui.pushButtonApplyClient.setText("Подтвердить\nизменение")
ui.pushButtonUseFilter.setText("Применить\nфильтры")
ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger(0))

status_edit = "not allow"
list_taken_id = []
status_client_edit = False
status_list_widget = False

message = QMessageBox()

dc = Clients()
dc.import_data("csv_files/Clients.csv")

dt = Tariffs()
dt.import_data("csv_files/Tariffs.csv")


def log_uncaught_exceptions(ex_cls, ex, tb):  # error catcher
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    text += ''.join(traceback.format_tb(tb))
    print(text)
    QtWidgets.QMessageBox.critical(None, 'Error', text)
    sys.exit()


sys.excepthook = log_uncaught_exceptions


def delete_rows(iterator):
    for i in range(iterator):
        ui.tableWidget.removeRow(i)


def show_table_data(dict_data, dict_t, dict_index, clear_status):
    global list_taken_id
    if clear_status:
        while ui.tableWidget.rowCount() > 0:
            delete_rows(ui.tableWidget.rowCount())
        list_taken_id = []
    ui.tableWidget.setRowCount(len(dict_data))
    dc.id_list_pos = []
    row = 0
    for key in dict_data:
        dc.id_list_pos.append(key)
        ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(dict_data[key].surname))
        ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(dict_data[key].name))
        ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(dict_data[key].patronymic))
        ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(dict_data[key].current_balance)))
        ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(dict_data[key].address))
        ui.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(dict_data[key].date.strftime("%d.%m.%Y")))
        id_tariff = dict_data[key].ID_tariff
        obj_tariff = dict_t[str(id_tariff)]
        ui.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(obj_tariff.name))
        ui.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(dict_data[key].active))
        list_taken_id.append(key)
        row += 1
    for key in dict_t:
        dict_index[dict_t[key].name] = key


def show_filtered_table_data():
    global status_client_edit
    status_client_edit = False
    dict_data = dc.dict_clients
    dict_t = dt.dict_tariffs
    dict_index = dt.id_dict_tariff
    tariff_filter = ui.comboBoxFilterTariff.currentText()
    active_filter = ui.comboBoxFilterActive.currentText()
    dict_new_data = {}
    if tariff_filter == "Не выбрано" and active_filter == "Не выбрано":
        show_table_data(dict_data=dict_data, dict_t=dict_t, dict_index=dict_index, clear_status=True)
        return
    elif tariff_filter != "Не выбрано" and active_filter == "Не выбрано":
        for key in dict_data.keys():
            if dict_t[dict_data[key].ID_tariff].name == tariff_filter:
                dict_new_data[key] = dict_data[key]
    elif tariff_filter == "Не выбрано" and active_filter != "Не выбрано":
        active_value = "0" if active_filter == "Неактивные" else "1"
        for key in dict_data.keys():
            if dict_data[key].active == active_value:
                dict_new_data[key] = dict_data[key]
    elif tariff_filter != "Не выбрано" and active_filter != "Не выбрано":
        active_value = "0" if active_filter == "Неактивные" else "1"
        for key in dict_data.keys():
            if dict_data[key].active == active_value and dict_t[dict_data[key].ID_tariff].name == tariff_filter:
                dict_new_data[key] = dict_data[key]
    show_table_data(dict_data=dict_new_data, dict_t=dict_t, dict_index=dict_index, clear_status=True)


def allow_edit_table():
    global status_edit
    if status_edit == "not allow":
        # ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger(2))
        ui.valueStatusEdit.setText("Разрешено")
        status_edit = "allow"
    elif status_edit == "allow":
        global status_client_edit
        status_client_edit = False
        ui.labelStatusV.setText("Запись не выбрана")
        # ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger(0))
        ui.valueStatusEdit.setText("Запрещено")
        status_edit = "not allow"


def if_has_int(value, len_value):
    count = 0
    for elem in value:
        if not elem.isdigit():
            count += 1
    if count == len_value:
        return False
    else:
        return True


def check_values(**kwargs):
    list_str = ["Фамилия", "Имя", "Отчество"]    # список текстовых полей
    for value in list_str:                       # проверка на пустоту или содержание числа
        if (not kwargs[value].strip()) or (if_has_int(kwargs[value], len(kwargs[value]))):
            return value
    if (not kwargs["Баланс"].strip()) or (not kwargs["Баланс"].isdigit()):    # проверка на пустоту или
        return "Баланс"                                                       # наличие буквы
    if not kwargs["Адрес"].strip():
        return "Адрес"
    try:
        datetime.strptime(kwargs["Дата"], "%d.%m.%Y")
    except ValueError:
        return "Дата"
    return "success"


def no_permission():
    message.setIcon(QMessageBox.Warning)
    message.setWindowTitle("Предупреждение")
    message.setText("Нет разрешения на редактирование\nИзмените статус редактирования таблицы")
    message.exec_()


def add_client():
    global status_edit
    global list_taken_id
    global status_client_edit
    status_client_edit = False
    ui.labelStatusV.setText("Запись не выбрана")
    if status_edit == "not allow":
        no_permission()
    else:
        new_id = 0
        g_surname = ui.lineEditSurname.text()
        g_name = ui.lineEditName.text()
        g_patronymic = ui.lineEditPatronymic.text()
        g_current_b = ui.lineEditCurrentB.text()
        g_address = ui.lineEditAddress.text()
        g_date = ui.lineEditDate.text()
        g_tariff = ui.comboBoxTariff.currentText()
        g_tariff_id = dt.id_dict_tariff[g_tariff]
        g_active = ui.comboBoxActive.currentText()
        result = check_values(Фамилия=g_surname, Имя=g_name, Отчество=g_patronymic, Баланс=g_current_b,
                              Адрес=g_address, Дата=g_date)
        if result == "success":
            set_taken_id = set(list_taken_id)
            list_max = max([int(x) for x in list_taken_id])
            for i in range(len(list_taken_id)):
                count = i + 1
                if str(count) not in set_taken_id:
                    new_id = count
                    break
                elif i == (len(list_taken_id) - 1):
                    new_id = list_max + 1
            dc.dict_clients[new_id] = Client(g_surname, g_name, g_patronymic, g_current_b, g_address,
                                             g_date, g_tariff_id, g_active)
            dc.export_data("csv_files/Clients.csv")
            dc.dict_clients = {}
            dc.id_list_pos = []
            list_taken_id = []
            dt.id_dict_tariff = {}
            dc.import_data("csv_files/Clients.csv")
            show_table_data(dict_data=dc.dict_clients, dict_t=dt.dict_tariffs,
                            dict_index=dt.id_dict_tariff, clear_status=False)
        else:
            message.setIcon(QMessageBox.Critical)
            message.setWindowTitle("Ошибка")
            message.setText(f"Ошибка при заполнении поля: {result}")
            if result == "Фамилия" or result == "Имя" or result == "Отчество":
                message.setDetailedText("Варианты возникновения ошибки:\n1. Поле пустое\n"
                                        "2. Поле пустое и в нём присутствуют пробелы\n" +
                                        "3. Поле заполнено, но в строке присутствуют цифры")
            elif result == "Баланс":
                message.setDetailedText("Варианты возникновения ошибки:\n1. Поле пустое\n"
                                        "2. Поле пустое и в нём присутствуют пробелы\n" +
                                        "3. Поле заполнено, но в строке присутствуют буквы\n" +
                                        "4. Поле заполнено, но число отрицательное\n")
            elif result == "Адрес":
                message.setDetailedText("Варианты возникновения ошибки:\n1. Поле пустое\n"
                                        "2. Поле пустое и в нём присутствуют пробелы")
            elif result == "Дата":
                message.setDetailedText("Варианты возникновения ошибки:\n1. Поле пустое\n"
                                        "2. Поле пустое и в нём присутствуют пробелы\n" +
                                        "3. Некорректно введена дата\n" +
                                        "Формат: день.месяц.год")
            message.exec_()


def choose_client():
    global status_client_edit
    status_client_edit = True
    current_row = ui.tableWidget.currentRow()
    if current_row != -1:
        dc.current_abonent_id = list_taken_id[ui.tableWidget.currentRow()]
        obj_class = dc.dict_clients[dc.id_list_pos[current_row]]
        ui.lineEditSurname.setText(obj_class.surname)
        ui.lineEditName.setText(obj_class.name)
        ui.lineEditPatronymic.setText(obj_class.patronymic)
        ui.lineEditCurrentB.setText(str(obj_class.current_balance))
        ui.lineEditAddress.setText(obj_class.address)
        ui.lineEditDate.setText(obj_class.date.strftime("%d.%m.%Y"))
        ui.comboBoxTariff.setCurrentText(dt.dict_tariffs[obj_class.ID_tariff].name)
        ui.comboBoxActive.setCurrentText(obj_class.active)
        ui.labelStatusV.setText("Запись выбрана")


def edit_client():
    global list_taken_id
    if status_edit == "not allow":
        no_permission()
    else:
        if status_client_edit and (dc.current_abonent_id == list_taken_id[ui.tableWidget.currentRow()]):
            g_surname = ui.lineEditSurname.text()
            g_name = ui.lineEditName.text()
            g_patronymic = ui.lineEditPatronymic.text()
            g_current_b = ui.lineEditCurrentB.text()
            g_address = ui.lineEditAddress.text()
            g_date = ui.lineEditDate.text()
            result = check_values(Фамилия=g_surname, Имя=g_name, Отчество=g_patronymic, Баланс=g_current_b,
                                  Адрес=g_address, Дата=g_date)
            if result == "success":
                current_abonent = dc.dict_clients[dc.current_abonent_id]
                current_abonent.surname = ui.lineEditSurname.text()
                current_abonent.name = ui.lineEditName.text()
                current_abonent.patronymic = ui.lineEditPatronymic.text()
                current_abonent.current_balance = ui.lineEditCurrentB.text()
                current_abonent.address = ui.lineEditAddress.text()
                current_abonent.date = datetime.strptime(ui.lineEditDate.text(), "%d.%m.%Y").date()
                current_abonent.ID_tariff = dt.id_dict_tariff[ui.comboBoxTariff.currentText()]
                current_abonent.active = ui.comboBoxActive.currentText()
                dc.export_data("csv_files/Clients.csv")
                dc.dict_clients = {}
                dc.id_list_pos = []
                list_taken_id = []
                dt.id_dict_tariff = {}
                dc.import_data("csv_files/Clients.csv")
                show_filtered_table_data()
            else:
                message.setIcon(QMessageBox.Critical)
                message.setWindowTitle("Ошибка")
                message.setText(f"Ошибка при заполнении поля: {result}")
                if result == "Фамилия" or result == "Имя" or result == "Отчество":
                    message.setDetailedText("Варианты возникновения ошибки:\n1. Поле пустое\n"
                                            "2. Поле пустое и в нём присутствуют пробелы\n" +
                                            "3. Поле заполнено, но в строке присутствуют цифры")
                elif result == "Баланс":
                    message.setDetailedText("Варианты возникновения ошибки:\n1. Поле пустое\n"
                                            "2. Поле пустое и в нём присутствуют пробелы\n" +
                                            "3. Поле заполнено, но в строке присутствуют буквы\n" +
                                            "4. Поле заполнено, но число отрицательное\n")
                elif result == "Адрес":
                    message.setDetailedText("Варианты возникновения ошибки:\n1. Поле пустое\n"
                                            "2. Поле пустое и в нём присутствуют пробелы")
                elif result == "Дата":
                    message.setDetailedText("Варианты возникновения ошибки:\n1. Поле пустое\n"
                                            "2. Поле пустое и в нём присутствуют пробелы\n" +
                                            "3. Некорректно введена дата\n" +
                                            "Формат: день.месяц.год")
                message.exec_()
            ui.labelStatusV.setText("Запись изменена")
        else:
            message.setIcon(QMessageBox.Critical)
            message.setWindowTitle("Ошибка")
            message.setText("Не выбрана запись для редактирования")
            message.setDetailedText("Выбранная для редактирования строка не совпадает с текущей выделенной")
            message.exec_()


def delete_client():
    global status_edit
    global list_taken_id
    global status_client_edit
    status_client_edit = False
    ui.labelStatusV.setText("Запись не выбрана")
    if status_edit == "not allow":
        no_permission()
    else:
        current_row = ui.tableWidget.currentRow()
        if current_row == -1:
            message.setIcon(QMessageBox.Warning)
            message.setWindowTitle("Предупреждение")
            message.setText("Не выбрана строка для удаления")
            message.exec_()
        else:
            del dc.dict_clients[dc.id_list_pos[current_row]]
            dc.export_data("csv_files/Clients.csv")
            dc.dict_clients = {}
            dc.id_list_pos = []
            list_taken_id = []
            dt.id_dict_tariff = {}
            dc.import_data("csv_files/Clients.csv")
            show_table_data(dict_data=dc.dict_clients, dict_t=dt.dict_tariffs,
                            dict_index=dt.id_dict_tariff, clear_status=False)


def install_date_today():
    ui.lineEditDate.setText(datetime.now().strftime("%d.%m.%Y"))


def update_box_tariff(dict_t):
    for key in dict_t.keys():
        ui.comboBoxTariff.addItem(str(dict_t[key].name))
        ui.comboBoxFilterTariff.addItem(str(dict_t[key].name))


def update_box_active():
    ui.comboBoxActive.addItem("1")
    ui.comboBoxActive.addItem("0")


update_box_tariff(dt.dict_tariffs)
update_box_active()
show_table_data(dict_data=dc.dict_clients, dict_t=dt.dict_tariffs, dict_index=dt.id_dict_tariff,
                clear_status=False)

ui.pushButtonEdit.clicked.connect(allow_edit_table)
ui.pushButtonAddClient.clicked.connect(add_client)
ui.pushButtonChooseClient.clicked.connect(choose_client)
ui.pushButtonApplyClient.clicked.connect(edit_client)
ui.pushButtonDeleteClient.clicked.connect(delete_client)
ui.pushButtonUseFilter.clicked.connect(show_filtered_table_data)
ui.pushButtonDateToday.clicked.connect(install_date_today)

ds = Services()
ds.import_data("csv_files/Services.csv")


def show_table_tariffs(dict_data, dict_services):
    ui.tableWidgetTariff.setRowCount(len(dict_data))
    str_services = ""
    row = 0
    for key in dict_data:
        ui.tableWidgetTariff.setItem(row, 0, QtWidgets.QTableWidgetItem(dict_data[key].name))
        for value in dict_data[key].services:
            str_services += dict_services[value].content + " , "
        ui.tableWidgetTariff.setItem(row, 1, QtWidgets.QTableWidgetItem(str_services))
        dict_data[key].get_price(dict_services)
        ui.tableWidgetTariff.setItem(row, 2, QtWidgets.QTableWidgetItem(str(dict_data[key].price)))
        str_services = ""
        row += 1


def show_table_services(dict_data):
    ui.tableWidgetService.setRowCount(len(dict_data))
    row = 0
    for key in dict_data:
        dc.id_list_pos.append(key)
        ui.tableWidgetService.setItem(row, 0, QtWidgets.QTableWidgetItem(dict_data[key].content))
        ui.tableWidgetService.setItem(row, 1, QtWidgets.QTableWidgetItem(str(dict_data[key].price)))
        row += 1


def accounting_payments():
    global status_list_widget
    if not status_list_widget:
        status_list_widget = True
    else:
        ui.listWidget0Days.clear()
        ui.listWidget1_2Days.clear()
        ui.listWidget3MoreDays.clear()
        ui.listWidgetOverdue.clear()
    ui.labelDateT.setText("Дата сегодня: " + datetime.now().strftime("%d.%m.%Y"))
    for value in dc.dict_clients.keys():
        timedelta = (dc.dict_clients[value].date - datetime.today().date()).days
        cur_client = dc.dict_clients[value]
        if timedelta >= 0:
            if timedelta == 0:
                ui.listWidget0Days.addItem(cur_client.surname + " " + cur_client.name + " " + cur_client.patronymic)
            elif 0 < timedelta <= 2:
                ui.listWidget1_2Days.addItem(cur_client.surname + " " + cur_client.name + " " + cur_client.patronymic +
                                             " - " + datetime.strftime(cur_client.date, "%d.%m.%Y"))
            else:
                ui.listWidget3MoreDays.addItem(cur_client.surname + " " + cur_client.name + " " + cur_client.patronymic
                                               + " - " + datetime.strftime(cur_client.date, "%d.%m.%Y"))
        else:
            ui.listWidgetOverdue.addItem(cur_client.surname + " " + cur_client.name + " " + cur_client.patronymic +
                                         " - " + datetime.strftime(cur_client.date, "%d.%m.%Y"))


ui.pushButtonCheckPayments.clicked.connect(accounting_payments)

show_table_tariffs(dt.dict_tariffs, ds.dict_services)
show_table_services(ds.dict_services)

sys.exit(app.exec_())
