import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
                            QApplication,
                            QMainWindow,
                            QLineEdit,
                            QGridLayout,
                            QVBoxLayout,
                            QHBoxLayout,
                            QWidget,
                            QLabel, 
                            QPushButton
                            )
## Constants
WINDOW_SIZE = 800

def loadItems():
    itemList = ["Provoxin", "Anatolin", "Dog Tags", "Gauze Bandages"]
    return itemList

class itemSelect(QMainWindow):
    def __init__(self):
        super(itemSelect, self).__init__()
        self.setWindowTitle("SIMple Inventory Manager")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        # Load internal Widgets
        self._topMenu()
        self._getItems()

    
    def _topMenu(self):
        BUTTON_HEIGHT = 75
        BUTTON_WIDTH = 200
        buttons = ["Add/Remove Items", "Settings"]
        self.topMenuButtonGrid = {}
        topMenuButtonLayout = QHBoxLayout()
        for button in buttons:
            self.topMenuButtonGrid[button] = QPushButton(f"{button}")
            self.topMenuButtonGrid[button].setFixedSize(BUTTON_WIDTH, BUTTON_HEIGHT)
            topMenuButtonLayout.addWidget(self.topMenuButtonGrid[button])
        self.generalLayout.addLayout(topMenuButtonLayout)

    def _getItems(self):
        COLUMNS = 3
        BUTTON_HEIGHT = 175
        BUTTON_WIDTH = 225
        self.buttonGrid = {}
        button_layout = QGridLayout()
        itemList = loadItems()
        col = 0
        row = 0
        for item in itemList:
            self.buttonGrid[item] = QPushButton(f"{item}")
            self.buttonGrid[item].setFixedSize(BUTTON_WIDTH, BUTTON_HEIGHT)
            button_layout.addWidget(self.buttonGrid[item], row, col)
            self.buttonGrid[item].clicked.connect(itemEditor(item).show)
            if col == 2:
                col = 0
                row += 1
            else:
                col += 1
        self.generalLayout.addLayout(button_layout)


class itemEditor(QWidget):
    def __init__(self, item):
        super(itemEditor, self).__init__()
        self.setWindowTitle(f"Editing {item}")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)

        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        
        self.itemEditing = QLabel(self)
        self.itemEditing.setText(item)

        self. _createNumberButtons()

    def _createDisplay(self):
        DISPLAY_HEIGHT = 45
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(False)
        self.generalLayout.addWidget(self.display)

    def _createNumberButtons(self):
        BUTTON_SIZE = 40
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
