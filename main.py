from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import pandas as pd
from styles.SettingsMenuStyle import Ui_settings
from styles.MainMenuStyle import Ui_MainWindow
import sys


class SettingsWindow(QMainWindow, Ui_settings):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.pressed.connect(self.apply)
        self.pushButton_2.pressed.connect(self.close_window)
        self.setMinimumSize(500, 400)
        self.data = None
        self.MainMenu = None

    def close_window(self):
        self.close()

    def apply(self):
        if self.LineEdit.text():
            self.MainMenu.delimiter = self.LineEdit.text()

        if self.data.empty or not self.tableWidget.selectedRanges():
            return

        book = {}
        headers = self.data.columns
        values = self.data.values.tolist()

        for selected in self.tableWidget.selectedRanges():
            for index in range(selected.leftColumn(), selected.rightColumn() + 1, 1):
                book[headers[index]] = [values[j][index] for j in range(selected.topRow(), selected.bottomRow(), 1)]

        self.data = pd.DataFrame(book)
        self.MainMenu.drawScreen.axes.cla()

        self.data.plot(ax=self.MainMenu.drawScreen.axes)
        self.MainMenu.drawScreen.draw()

    def update(self):
        self.LineEdit.setText(self.MainMenu.delimiter)
        if self.data.empty:
            return
        self.tableWidget.setColumnCount(len(self.data.columns))
        self.tableWidget.setRowCount(self.data.shape[0])

        self.tableWidget.setHorizontalHeaderLabels(self.data.columns)

        values = self.data.values.tolist()
        for i, val in enumerate(values):
            for j, it in enumerate(val):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(it)))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setMinimumSize(500, 400)
        self.w = None
        self.delimiter = ','
        self.data = pd.DataFrame({})

        # Меню "Файл"
        bar = self.menuBar()
        self.file = bar.addMenu("Файл")

        open = QAction("Открыть", self)
        open.triggered.connect(self.open)
        self.file.addAction(open)

        cl = QAction("Закрыть", self)
        cl.triggered.connect(self.close_file)
        self.file.addAction(cl)

        open = QAction("Настройки", self)
        open.triggered.connect(self.settings)
        self.file.addAction(open)

        bar.setFixedSize(75, 40)
        font = bar.font()
        font.setPointSize(12)
        bar.setFont(font)

        self.horizontalLayout.addWidget(bar)
        self.horizontalLayout.addWidget(self.toolbar)

    def close_file(self):
        self.data = pd.DataFrame({})
        self.drawScreen.axes.cla()
        self.drawScreen.draw()

    def open(self):
        try:
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getOpenFileName(None, "Открыть файл")
            self.data = pd.read_csv(file_path, delimiter=self.delimiter)
            self.update()
        except Exception:
            pass

    def update(self):
        if self.data.empty:
            return
        self.drawScreen.axes.cla()
        self.data.plot(ax=self.drawScreen.axes)
        self.drawScreen.draw()

    def settings(self):
        if self.w is None:
            self.w = SettingsWindow()
        self.w.MainMenu = self
        self.w.data = self.data
        self.w.update()
        self.w.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
