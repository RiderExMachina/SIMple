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



class itemSelect(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SIMple Inventory Manager")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
    
    def _getItems(self):
        loadItems()

class itemEditor(QMainWindow):
    
    def _createButtons(self):
        self.buttonMap = {}
        number_pad = QGridLayout
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
