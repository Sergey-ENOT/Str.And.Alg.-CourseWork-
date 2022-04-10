# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\..\DB_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Add_interface import Ui_NewWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1041, 623)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(950, 180, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(10, 220, 1021, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(1021, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(1021, 16777215))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidget.setDragDropOverwriteMode(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 281, 42))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonEdit = QtWidgets.QPushButton(self.widget)
        self.pushButtonEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonEdit.sizePolicy().hasHeightForWidth())
        self.pushButtonEdit.setSizePolicy(sizePolicy)
        self.pushButtonEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.horizontalLayout.addWidget(self.pushButtonEdit)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.statusEdit = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusEdit.sizePolicy().hasHeightForWidth())
        self.statusEdit.setSizePolicy(sizePolicy)
        self.statusEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statusEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.statusEdit.setObjectName("statusEdit")
        self.verticalLayout.addWidget(self.statusEdit)
        self.valueStatusEdit = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valueStatusEdit.sizePolicy().hasHeightForWidth())
        self.valueStatusEdit.setSizePolicy(sizePolicy)
        self.valueStatusEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.valueStatusEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.valueStatusEdit.setObjectName("valueStatusEdit")
        self.verticalLayout.addWidget(self.valueStatusEdit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(440, 10, 97, 88))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButtonAdd = QtWidgets.QPushButton(self.widget1)
        self.pushButtonAdd.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAdd.sizePolicy().hasHeightForWidth())
        self.pushButtonAdd.setSizePolicy(sizePolicy)
        self.pushButtonAdd.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.verticalLayout_2.addWidget(self.pushButtonAdd)
        self.pushButtonDelete = QtWidgets.QPushButton(self.widget1)
        self.pushButtonDelete.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDelete.sizePolicy().hasHeightForWidth())
        self.pushButtonDelete.setSizePolicy(sizePolicy)
        self.pushButtonDelete.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.verticalLayout_2.addWidget(self.pushButtonDelete)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(10, 490, 61, 81))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelName = QtWidgets.QLabel(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelName.sizePolicy().hasHeightForWidth())
        self.labelName.setSizePolicy(sizePolicy)
        self.labelName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelName.setObjectName("labelName")
        self.verticalLayout_3.addWidget(self.labelName)
        self.labelSurname = QtWidgets.QLabel(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSurname.sizePolicy().hasHeightForWidth())
        self.labelSurname.setSizePolicy(sizePolicy)
        self.labelSurname.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelSurname.setObjectName("labelSurname")
        self.verticalLayout_3.addWidget(self.labelSurname)
        self.labelPatronymic = QtWidgets.QLabel(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPatronymic.sizePolicy().hasHeightForWidth())
        self.labelPatronymic.setSizePolicy(sizePolicy)
        self.labelPatronymic.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPatronymic.setObjectName("labelPatronymic")
        self.verticalLayout_3.addWidget(self.labelPatronymic)
        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(80, 490, 135, 81))
        self.widget3.setObjectName("widget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEditSurname = QtWidgets.QLineEdit(self.widget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSurname.sizePolicy().hasHeightForWidth())
        self.lineEditSurname.setSizePolicy(sizePolicy)
        self.lineEditSurname.setObjectName("lineEditSurname")
        self.verticalLayout_4.addWidget(self.lineEditSurname)
        self.lineEditName = QtWidgets.QLineEdit(self.widget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditName.sizePolicy().hasHeightForWidth())
        self.lineEditName.setSizePolicy(sizePolicy)
        self.lineEditName.setObjectName("lineEditName")
        self.verticalLayout_4.addWidget(self.lineEditName)
        self.lineEditPatronymic = QtWidgets.QLineEdit(self.widget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditPatronymic.sizePolicy().hasHeightForWidth())
        self.lineEditPatronymic.setSizePolicy(sizePolicy)
        self.lineEditPatronymic.setObjectName("lineEditPatronymic")
        self.verticalLayout_4.addWidget(self.lineEditPatronymic)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1041, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButtonAdd.clicked.connect(self.add_data)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Print Data"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Фамилия"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Отчество"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Текущий баланс"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Адрес"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Тариф"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Активность"))
        self.pushButtonEdit.setText(_translate("MainWindow", "Редактировать"))
        self.statusEdit.setText(_translate("MainWindow", "Статус редактирования:"))
        self.valueStatusEdit.setText(_translate("MainWindow", "Запрещено"))
        self.pushButtonAdd.setText(_translate("MainWindow", "Добавить запись"))
        self.pushButtonDelete.setText(_translate("MainWindow", "Удалить запись"))
        self.labelName.setText(_translate("MainWindow", "Фамилия:"))
        self.labelSurname.setText(_translate("MainWindow", "Имя:"))
        self.labelPatronymic.setText(_translate("MainWindow", "Отчество:"))

    def add_data(self):
        self.n_w = QtWidgets.QWidget()
        self.n_w.show()


class MyNewWindow(QtWidgets.QWidget, Ui_NewWindow):
    def __init__(self, parent=None):
        super(MyNewWindow, self).__init__(parent)
        self.setupUi(self)


class Main(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.pushButtonAdd.clicked.connect(self.on_clicked)

    def on_clicked(self):
        self.window = MyNewWindow()
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    w = Main()
    w.show()
    sys.exit(app.exec_())
