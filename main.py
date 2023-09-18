from PyQt5.Qt import *
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar, FigureCanvasQTAgg
from PyQt5 import QtCore, QtWidgets
from matplotlib.figure import Figure
import pandas as pd
import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Plot")
        MainWindow.resize(800, 600)
        self.w = None
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

        bar = self.menuBar()
        self.file = bar.addMenu("Файл")

        open = QAction("Открыть", self)
        #save.setShortcut("Ctrl+S")
        open.triggered.connect(self.open)
        self.file.addAction(open)

        open = QAction("Настройки", self)
        # save.setShortcut("Ctrl+S")
        open.triggered.connect(self.settings)
        self.file.addAction(open)



        save = QAction("Save", self)
        save.setShortcut("Ctrl+S")
        self.file.addAction(save)

        edit = self.file.addMenu("Edit")
        edit.addAction("copy")
        edit.addAction("paste")

        quit = QAction(QIcon("D:/_Qt/__Qt/img/exit.png"), "Quit", self)
        quit.setShortcut('Ctrl+Q')

        self.file.addAction(quit)

        #self.file.triggered[QAction].connect(self.processtrigger)

        bar.setFixedSize(75, 40)
        font = bar.font()
        font.setPointSize(12)
        bar.setFont(font)






        self.horizontalLayout.addWidget(bar)

        self.horizontalLayout.addWidget(self.toolbar)
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

    def open(self):
        print('open')
        self.drawScreen.axes.cla()



        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Открыть файл")

    def settings(self):
        print('settings')
        if self.w is None:
            self.w = AnotherWindow()
        self.w.show()
class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)





class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setMinimumSize(500, 400)

    def func(self):

        self.drawScreen.axes.cla()

        if self.lineEdit.text() == "":
            delimiter = ","
        else:
            delimiter = self.lineEdit.text()

        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Открыть файл")

        if self.lineEdit2.text() != "" and self.lineEdit2.text().isdigit():
            data = pd.read_csv(file_path, delimiter=delimiter)
            nrows = int(self.lineEdit2.text())
            if data.shape[0] > nrows:
                data = pd.read_csv(file_path, delimiter=delimiter, nrows=nrows)
        else:
            data = pd.read_csv(file_path, delimiter=delimiter)

        data.plot(ax=self.drawScreen.axes)

        self.drawScreen.draw()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
