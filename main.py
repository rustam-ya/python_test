import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QTableWidget


class Window(QWidget):
    def __init__(self, basa_d):
        super().__init__()
        uic.loadUi('ui1.ui', self)
        self.basa_d = basa_d
        self.basa_cursor = self.basa_d.cursor()
        result = self.basa_cursor.execute("""SELECT * FROM menu_bar""").fetchall()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Сорт", "Степень обжарка", "Тип", "Описание", "Цена", "Объём"])
        self.tableWidget.setRowCount(len(result))
        for i in range(len(result)):
            b = self.basa_cursor.execute("""SELECT * FROM menu_bar WHERE id = (?)""", (result[i][3],)).fetchall()
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(result[i][0])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(result[i][1])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(result[i][2])))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(result[i][3])))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(str(result[i][4])))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(str(result[i][5])))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(str(result[i][6])))
        result = self.basa_cursor.execute("""SELECT * FROM genres""").fetchall()
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setHorizontalHeaderLabels(["ID", "Название"])
        self.tableWidget_2.setRowCount(len(result))
        for i in range(len(result)):
            self.tableWidget_2.setItem(i, 0, QTableWidgetItem(str(result[i][0])))
            self.tableWidget_2.setItem(i, 1, QTableWidgetItem(str(result[i][1])))

if __name__ == '__main__':
    basa_d = sqlite3.connect('coffee.sqlite')
    basa_cursor = basa_d.cursor()
    app = QApplication(sys.argv)
    os = Window(basa_d)
    os.show()
    sys.exit(app.exec())
