from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar, FigureCanvasQTAgg
from PyQt5 import QtCore, QtWidgets, QtGui
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Plot")
        MainWindow.resize(800, 600)

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
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Графики"))
