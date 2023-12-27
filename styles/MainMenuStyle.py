from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar, FigureCanvasQTAgg
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QAction
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
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        self.menubar.setFixedSize(75, 40)

        self.file = self.menubar.addMenu("Файл")
        self.openAction = QAction("Открыть", self)

        self.file.addAction(self.openAction)

        self.closeAction = QAction("Закрыть", self)

        self.file.addAction(self.closeAction)

        self.settingsAction = QAction("Настройки", self)

        self.file.addAction(self.settingsAction)

        # задаем размер и шрифт меню

        font = self.menubar.font()
        font.setPointSize(14)
        font.setBold(True)
        self.menubar.setFont(font)


        # добавляем в layout
        self.horizontalLayout.addWidget(self.menubar)
        self.horizontalLayout.addWidget(self.toolbar)



        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Графики"))
