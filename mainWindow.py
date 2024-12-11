from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QTableWidget,
    QHeaderView,
    QTableWidgetItem,
    QPushButton
)
import db

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("kr2")
        self.__uiInit()

    def show(self):
        self.__loadData()
        super().show()

    def __uiInit(self):
        self.__mainLayoutInit()
        self.__buttonsInit()
        self.__tableInit()

    def __mainLayoutInit(self):
        self.__centralWidget = QWidget()
        self.__mainLayout = QVBoxLayout()
        self.__centralWidget.setLayout(self.__mainLayout)
        self.setCentralWidget(self.__centralWidget)
        
    def __buttonsInit(self):
        self.__buttonsLayout = QHBoxLayout()
        self.__mainLayout.addLayout(self.__buttonsLayout)

        self.__editButton = QPushButton("edit", clicked=lambda: print("edit"))
        self.__reportButton = QPushButton("report", clicked=lambda: print("report"))
        self.__buttonsLayout.addWidget(self.__editButton)
        self.__buttonsLayout.addWidget(self.__reportButton)

    def __tableInit(self):
        self.__table = QTableWidget(0, 4)
        self.__table.setHorizontalHeaderLabels(["Клиент", "Автомобиль", "Дата начала", "Количество дней"])
        self.__table.setEditTriggers(QTableWidget.NoEditTriggers)
        header = self.__table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.__mainLayout.addWidget(self.__table)

    def __loadData(self):
        rentals = db.getRentals()

        height = len(rentals)
        width = len(rentals[0])

        self.__table.setRowCount(height)
        for y in range(0, height):
            for x in range(0, width):
                self.__table.setItem(y, x, QTableWidgetItem(str(rentals[y][x])))
