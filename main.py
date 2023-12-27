from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import pandas as pd
from styles.SettingsMenuStyle import Ui_settings
from styles.MainMenuStyle import Ui_MainWindow
from styles.DataMenuStyle import Ui_data
import sys


class DataWinwow(QMainWindow, Ui_data):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # подключаем кнопки к функциям

        self.setMinimumSize(500, 400)
        # задаем data, где будет храниться dataframe
        self.data = None
        self.pushButton.clicked.connect(self.apply)
        self.pushButton_2.clicked.connect(self.close)
        self.SettingsMenu = None

    def apply(self):  # функция принять
        print("ok")


        # если данных нет, или ничего не выбрано, то выходим из функции
        if self.data.empty or not self.tableWidget.selectedRanges():
            return

        # создаем новый dataframe с выбранными значениями
        book = {}  # словарь для значений
        headers = self.MainMenu.data.columns  # список заголовков
        values = self.MainMenu.data.values.tolist()  # вложенный список всех значений

        for selected in self.tableWidget.selectedRanges():  # бежим по выбранным значениям и добавляем их в book
            for index in range(selected.leftColumn(), selected.rightColumn() + 1, 1):
                book[headers[index]] = [values[j][index] for j in range(selected.topRow(), selected.bottomRow(), 1)]

        self.data = pd.DataFrame(book)  # переводим book в dataframe
        self.MainMenu.drawScreen.axes.cla()  # очищаем холст

        self.data.plot(ax=self.MainMenu.drawScreen.axes)  # рисуем график
        self.MainMenu.drawScreen.draw()  # обновляем холст

    def update(self):  # функция обновления окна
        # устанавливаем в строку текущий разделитель
        if self.data.empty:  # если данных нет, то заканчиваем функцию
            return
        self.tableWidget.setColumnCount(len(self.data.columns))  # задаем количество столбцов и строк
        self.tableWidget.setRowCount(self.data.shape[0])

        self.tableWidget.setHorizontalHeaderLabels(self.data.columns)  # задаем заголовки

        values = self.data.values.tolist()  # считываем все данные и добавляем их в таблицу
        for i, val in enumerate(values):
            for j, it in enumerate(val):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(it)))


class SettingsWindow(QMainWindow, Ui_settings):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setMinimumSize(500, 400)


        self.pushButton_3.clicked.connect(self.apply)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.open)

        self.data = None
        self.MainMenu = None
        self.DataMenu = None

    def close_window(self):
        self.close()

    def apply(self):
        pass
        if self.lineEdit.text():  # если есть разделитель, то считываем и обновляем его
            self.MainMenu.delimiter = self.lineEdit.text()
    def open(self):
        if self.DataMenu is None:
            self.DataMenu = DataWinwow()  # создаем объект класса меню настроек
        self.DataMenu.SettingsMenu = self
        self.DataMenu.data = self.data  # передаем ему данные и объект класса основного окна
        self.DataMenu.update()
        self.DataMenu.show()



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setMinimumSize(500, 400)
        self.SettingWindow = None  # создаем переменную для окна настройки
        self.delimiter = ','  # переменная для хранения разделителя
        self.data = pd.DataFrame({})  # переменная для dataframe

        # добавляем пункты меню и привязываем их к функциям

        self.openAction.triggered.connect(self.open)
        self.closeAction.triggered.connect(self.close_file)
        self.settingsAction.triggered.connect(self.settings)

    def close_file(self):  # функция закрытия файла очищает холст и данные
        self.data = pd.DataFrame({})
        self.drawScreen.axes.cla()
        self.drawScreen.draw()

    def open(self):  # функция открытия считывает путь файла и данные
        try:
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getOpenFileName(None, "Открыть файл")
            self.data = pd.read_csv(file_path, delimiter=self.delimiter)
            # self.update()
            self.settings()
        except Exception:
            pass

    def update(self):  # функция обновления рисует холст
        if self.data.empty:
            return
        self.drawScreen.axes.cla()
        self.data.plot(ax=self.drawScreen.axes)
        self.drawScreen.draw()

    def settings(self):  # функция вызова меню настроек
        if self.SettingWindow is None:
            self.SettingWindow = SettingsWindow()  # создаем объект класса меню настроек
        self.SettingWindow.MainMenu = self
        self.SettingWindow.data = self.data  # передаем ему данные и объект класса основного окна
        self.SettingWindow.update()
        self.SettingWindow.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
