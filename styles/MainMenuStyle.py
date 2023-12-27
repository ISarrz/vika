from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar, FigureCanvasQTAgg
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QAction, QMenu, QPushButton, QVBoxLayout
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):  # файл стиля, подключаем различные виджеты
        MainWindow.setObjectName("Plot")
        MainWindow.resize(800, 600)
        self.setMinimumSize(500, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.setWindowIcon(QtGui.QIcon('icon.jpg'))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.drawScreen = MplCanvas(self, width=5, height=4, dpi=100)
        self.verticalLayout.addWidget(self.drawScreen)

        self.toolbar = NavigationToolbar(self.drawScreen, self)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menu = QMenu()
        self.openAction = QAction("Открыть", self)
        self.menu.addAction(self.openAction)
        self.closeAction = QAction("Закрыть", self)
        self.menu.addAction(self.closeAction)
        self.settingsAction = QAction("Настройки", self)
        self.menu.addAction(self.settingsAction)

        self.pushButton = QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("ФАЙЛ")
        font = self.pushButton.font()
        font.setPointSize(14)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.pressed.connect(self.open_menu)
        self.pushButton.setChecked(True)


        self.menu.close()

        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addWidget(self.toolbar)

        self.check = False

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def open_menu(self):

        self.menu.move(self.frameGeometry().topLeft().x() + 2,
                       self.frameGeometry().topLeft().y() + 80)

        self.menu.exec_()
        self.pushButton.clearFocus()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Графики"))
