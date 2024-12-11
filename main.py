from mainWindow import MainWindow
from PySide6.QtWidgets import QApplication
import db

if __name__ == "__main__":
    db.connect()
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
    db.close()