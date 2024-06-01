import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
                            QApplication,
                            QMainWindow,
                            QLineEdit,
                            QGridLayout,
                            QVBoxLayout,
                            QHBoxLayout,
                            QLabel, 
                            QWidget, 
                            QPushButton
                            )
## Constants
WINDOW_SIZE = 800

def loadItems():
    itemList = ["Provoxin", "Anatolin", "Dog Tags", "Gauze Bandages"]
    return itemList

class itemSelect(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SIMple Inventory Manager")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._getItems()

    def _getItems(self):
        COLUMNS = 3
        BUTTON_HEIGHT = 175
        BUTTON_WIDTH = 225
        self.buttonGrid = {}
        button_layout = QGridLayout()
        itemList = loadItems()
        for col in range(0, COLUMNS):
            for row, item in enumerate(itemList):
                self.buttonGrid[item] = QPushButton(f"{item} - {row}, {col}")
                self.buttonGrid[item].setFixedSize(BUTTON_WIDTH, BUTTON_HEIGHT)
                button_layout.addWidget(self.buttonGrid[item], row, col)
        self.generalLayout.addLayout(button_layout)


class itemEditor(QMainWindow):
    
    def _createNumberButtons(self):
        self.buttonMap = {}
        number_pad = QGridLayout()
        keyboard = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["←", "0", "↵"]
        ]
        for row, keys in enumerate(keyboard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                number_pad.addWidget(self.buttonMap[key], row, col)
        
        self.generalLayout.addLayout(number_pad)

def main():
    app = QApplication([])
    appWindow = itemSelect()
    appWindow.show()

    #item = "Test Item"
    #item_name = QLabel(item)
    #refresh = QPushButton()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
