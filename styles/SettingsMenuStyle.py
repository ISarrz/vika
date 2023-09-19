from PyQt5 import QtCore, QtWidgets


class Ui_settings(object):
    def setupUi(self, settings):  # файл стиля, подключаем различные виджеты
        settings.setObjectName("settings")
        settings.resize(759, 600)
        self.centralwidget = QtWidgets.QWidget(settings)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("LineEdit")
        self.label.setText("Разделитель csv")
        self.horizontalLayout.addWidget(self.label)

        self.LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.LineEdit.setText(",")

        self.LineEdit.setObjectName("LineEdit")
        self.horizontalLayout.addWidget(self.LineEdit)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        settings.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(settings)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 759, 18))
        self.menubar.setObjectName("menubar")
        settings.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(settings)
        self.statusbar.setObjectName("statusbar")
        settings.setStatusBar(self.statusbar)

        self.retranslateUi(settings)
        QtCore.QMetaObject.connectSlotsByName(settings)

    def retranslateUi(self, settings):
        _translate = QtCore.QCoreApplication.translate
        settings.setWindowTitle(_translate("settings", "Настройки"))
        self.pushButton_2.setText(_translate("settings", "Ок"))
        self.pushButton.setText(_translate("settings", "Принять"))
