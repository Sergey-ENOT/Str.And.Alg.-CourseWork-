# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\..\DB_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1061, 888)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1051, 841))
        self.tabWidget.setObjectName("tabWidget")
        self.tabClient = QtWidgets.QWidget()
        self.tabClient.setObjectName("tabClient")
        self.layoutWidget = QtWidgets.QWidget(self.tabClient)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 281, 43))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonEdit = QtWidgets.QPushButton(self.layoutWidget)
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
        self.statusEdit = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusEdit.sizePolicy().hasHeightForWidth())
        self.statusEdit.setSizePolicy(sizePolicy)
        self.statusEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statusEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.statusEdit.setObjectName("statusEdit")
        self.verticalLayout.addWidget(self.statusEdit)
        self.valueStatusEdit = QtWidgets.QLabel(self.layoutWidget)
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
        self.pushButton = QtWidgets.QPushButton(self.tabClient)
        self.pushButton.setGeometry(QtCore.QRect(940, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.tabClient)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(0, 170, 1041, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(1677777, 16777215))
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
        self.layoutWidget1 = QtWidgets.QWidget(self.tabClient)
        self.layoutWidget1.setGeometry(QtCore.QRect(900, 430, 126, 134))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButtonAddClient = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButtonAddClient.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAddClient.sizePolicy().hasHeightForWidth())
        self.pushButtonAddClient.setSizePolicy(sizePolicy)
        self.pushButtonAddClient.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButtonAddClient.setObjectName("pushButtonAddClient")
        self.verticalLayout_4.addWidget(self.pushButtonAddClient)
        self.pushButtonEditClient = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButtonEditClient.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButtonEditClient.setObjectName("pushButtonEditClient")
        self.verticalLayout_4.addWidget(self.pushButtonEditClient)
        self.pushButtonDeleteClient = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButtonDeleteClient.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDeleteClient.sizePolicy().hasHeightForWidth())
        self.pushButtonDeleteClient.setSizePolicy(sizePolicy)
        self.pushButtonDeleteClient.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButtonDeleteClient.setObjectName("pushButtonDeleteClient")
        self.verticalLayout_4.addWidget(self.pushButtonDeleteClient)
        self.layoutWidget2 = QtWidgets.QWidget(self.tabClient)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 430, 501, 289))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget2)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.labelName = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelName.sizePolicy().hasHeightForWidth())
        self.labelName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelName.setFont(font)
        self.labelName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelName.setObjectName("labelName")
        self.verticalLayout_7.addWidget(self.labelName)
        self.labelSurname = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSurname.sizePolicy().hasHeightForWidth())
        self.labelSurname.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelSurname.setFont(font)
        self.labelSurname.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelSurname.setObjectName("labelSurname")
        self.verticalLayout_7.addWidget(self.labelSurname)
        self.labelPatronymic = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPatronymic.sizePolicy().hasHeightForWidth())
        self.labelPatronymic.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelPatronymic.setFont(font)
        self.labelPatronymic.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPatronymic.setObjectName("labelPatronymic")
        self.verticalLayout_7.addWidget(self.labelPatronymic)
        self.labelCurrentB = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCurrentB.sizePolicy().hasHeightForWidth())
        self.labelCurrentB.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCurrentB.setFont(font)
        self.labelCurrentB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelCurrentB.setObjectName("labelCurrentB")
        self.verticalLayout_7.addWidget(self.labelCurrentB)
        self.labelDate = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDate.sizePolicy().hasHeightForWidth())
        self.labelDate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelDate.setFont(font)
        self.labelDate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelDate.setObjectName("labelDate")
        self.verticalLayout_7.addWidget(self.labelDate)
        self.labelTariff = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTariff.setFont(font)
        self.labelTariff.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTariff.setObjectName("labelTariff")
        self.verticalLayout_7.addWidget(self.labelTariff)
        self.labelActive = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelActive.setFont(font)
        self.labelActive.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelActive.setObjectName("labelActive")
        self.verticalLayout_7.addWidget(self.labelActive)
        self.labelAddress = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelAddress.sizePolicy().hasHeightForWidth())
        self.labelAddress.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelAddress.setFont(font)
        self.labelAddress.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelAddress.setObjectName("labelAddress")
        self.verticalLayout_7.addWidget(self.labelAddress)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEditSurname = QtWidgets.QLineEdit(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSurname.sizePolicy().hasHeightForWidth())
        self.lineEditSurname.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditSurname.setFont(font)
        self.lineEditSurname.setObjectName("lineEditSurname")
        self.verticalLayout_6.addWidget(self.lineEditSurname)
        self.lineEditName = QtWidgets.QLineEdit(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditName.sizePolicy().hasHeightForWidth())
        self.lineEditName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditName.setFont(font)
        self.lineEditName.setObjectName("lineEditName")
        self.verticalLayout_6.addWidget(self.lineEditName)
        self.lineEditPatronymic = QtWidgets.QLineEdit(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditPatronymic.sizePolicy().hasHeightForWidth())
        self.lineEditPatronymic.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditPatronymic.setFont(font)
        self.lineEditPatronymic.setObjectName("lineEditPatronymic")
        self.verticalLayout_6.addWidget(self.lineEditPatronymic)
        self.lineEditCurrentB = QtWidgets.QLineEdit(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditCurrentB.sizePolicy().hasHeightForWidth())
        self.lineEditCurrentB.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditCurrentB.setFont(font)
        self.lineEditCurrentB.setObjectName("lineEditCurrentB")
        self.verticalLayout_6.addWidget(self.lineEditCurrentB)
        self.lineEditDate = QtWidgets.QLineEdit(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditDate.sizePolicy().hasHeightForWidth())
        self.lineEditDate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditDate.setFont(font)
        self.lineEditDate.setObjectName("lineEditDate")
        self.verticalLayout_6.addWidget(self.lineEditDate)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBoxTariff = QtWidgets.QComboBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxTariff.setFont(font)
        self.comboBoxTariff.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBoxTariff.setObjectName("comboBoxTariff")
        self.verticalLayout_3.addWidget(self.comboBoxTariff)
        self.comboBoxActive = QtWidgets.QComboBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxActive.setFont(font)
        self.comboBoxActive.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBoxActive.setObjectName("comboBoxActive")
        self.verticalLayout_3.addWidget(self.comboBoxActive)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.lineEditAddress = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEditAddress.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditAddress.sizePolicy().hasHeightForWidth())
        self.lineEditAddress.setSizePolicy(sizePolicy)
        self.lineEditAddress.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEditAddress.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditAddress.setFont(font)
        self.lineEditAddress.setObjectName("lineEditAddress")
        self.verticalLayout_6.addWidget(self.lineEditAddress)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_6)
        self.layoutWidget3 = QtWidgets.QWidget(self.tabClient)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 90, 291, 51))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget3)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelFilterTariff = QtWidgets.QLabel(self.layoutWidget3)
        self.labelFilterTariff.setAlignment(QtCore.Qt.AlignCenter)
        self.labelFilterTariff.setObjectName("labelFilterTariff")
        self.verticalLayout_5.addWidget(self.labelFilterTariff)
        self.labelFilterActive = QtWidgets.QLabel(self.layoutWidget3)
        self.labelFilterActive.setObjectName("labelFilterActive")
        self.verticalLayout_5.addWidget(self.labelFilterActive)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBoxFilterTariff = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBoxFilterTariff.setObjectName("comboBoxFilterTariff")
        self.comboBoxFilterTariff.addItem("")
        self.verticalLayout_2.addWidget(self.comboBoxFilterTariff)
        self.comboBoxFilterActive = QtWidgets.QComboBox(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxFilterActive.sizePolicy().hasHeightForWidth())
        self.comboBoxFilterActive.setSizePolicy(sizePolicy)
        self.comboBoxFilterActive.setObjectName("comboBoxFilterActive")
        self.comboBoxFilterActive.addItem("")
        self.comboBoxFilterActive.addItem("")
        self.comboBoxFilterActive.addItem("")
        self.verticalLayout_2.addWidget(self.comboBoxFilterActive)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_2)
        self.pushButtonUseFilter = QtWidgets.QPushButton(self.tabClient)
        self.pushButtonUseFilter.setGeometry(QtCore.QRect(320, 90, 101, 51))
        self.pushButtonUseFilter.setAutoRepeat(False)
        self.pushButtonUseFilter.setAutoDefault(False)
        self.pushButtonUseFilter.setObjectName("pushButtonUseFilter")
        self.tabWidget.addTab(self.tabClient, "")
        self.tabTariff = QtWidgets.QWidget()
        self.tabTariff.setObjectName("tabTariff")
        self.label_3 = QtWidgets.QLabel(self.tabTariff)
        self.label_3.setGeometry(QtCore.QRect(140, 160, 47, 13))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.tabTariff)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 120, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tabTariff, "")
        self.tabService = QtWidgets.QWidget()
        self.tabService.setObjectName("tabService")
        self.tabWidget.addTab(self.tabService, "")
        self.tabImage = QtWidgets.QWidget()
        self.tabImage.setObjectName("tabImage")
        self.labelImage = QtWidgets.QLabel(self.tabImage)
        self.labelImage.setGeometry(QtCore.QRect(6, 2, 1021, 561))
        self.labelImage.setText("")
        self.labelImage.setPixmap(QtGui.QPixmap("..\\..\\739010.png"))
        self.labelImage.setScaledContents(True)
        self.labelImage.setObjectName("labelImage")
        self.tabWidget.addTab(self.tabImage, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1061, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonEdit.setText(_translate("MainWindow", "Редактировать"))
        self.statusEdit.setText(_translate("MainWindow", "Статус редактирования:"))
        self.valueStatusEdit.setText(_translate("MainWindow", "Запрещено"))
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
        self.pushButtonAddClient.setText(_translate("MainWindow", "Добавить запись"))
        self.pushButtonEditClient.setText(_translate("MainWindow", "Редактировать запись"))
        self.pushButtonDeleteClient.setText(_translate("MainWindow", "Удалить запись"))
        self.labelName.setText(_translate("MainWindow", "Фамилия:"))
        self.labelSurname.setText(_translate("MainWindow", "Имя:"))
        self.labelPatronymic.setText(_translate("MainWindow", "Отчество:"))
        self.labelCurrentB.setText(_translate("MainWindow", "Баланс:"))
        self.labelDate.setText(_translate("MainWindow", "Дата:"))
        self.labelTariff.setText(_translate("MainWindow", "Тариф:"))
        self.labelActive.setText(_translate("MainWindow", "Активность:"))
        self.labelAddress.setText(_translate("MainWindow", "Адрес:"))
        self.labelFilterTariff.setText(_translate("MainWindow", "Фильтр по тарифу:"))
        self.labelFilterActive.setText(_translate("MainWindow", "Фильтр по активности:"))
        self.comboBoxFilterTariff.setItemText(0, _translate("MainWindow", "Не выбрано"))
        self.comboBoxFilterActive.setItemText(0, _translate("MainWindow", "Не выбрано"))
        self.comboBoxFilterActive.setItemText(1, _translate("MainWindow", "Активные"))
        self.comboBoxFilterActive.setItemText(2, _translate("MainWindow", "Неактивные"))
        self.pushButtonUseFilter.setText(_translate("MainWindow", "прим.фильтры"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabClient), _translate("MainWindow", "База клиентов"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTariff), _translate("MainWindow", "База тарифов"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabService), _translate("MainWindow", "База услуг"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabImage), _translate("MainWindow", "Изображение"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
