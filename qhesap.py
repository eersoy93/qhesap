# QHesap main script
# Copyright (C) 2022 Erdem Ersoy (eersoy93)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QGridLayout,
                             QLineEdit, QPushButton, QWidget)

class QHesap(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.setLayout(self.grid)

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.grid.addWidget(self.lineEdit, 0, 0, 1, 4)

        self.button_names = ["CLS", "←", "ABOUT", "ABOUT QT",
                             "7", "8", "9", "/",
                             "4", "5", "6", "*",
                             "1", "2", "3", "-",
                             "0", ".", "=", "+"]

        self.button_positions = [(i, j) for i in range(1, 6) for j in range(4)]

        self.buttons = list()

        for name in self.button_names:
            self.buttons.append(QPushButton(name))

            if name == "CLS":
                self.buttons[-1].clicked.connect(self.CLS)
            elif name == "←":
                self.buttons[-1].clicked.connect(self.BACKSPACE)
            elif name == "ABOUT":
                self.buttons[-1].clicked.connect(self.ABOUT)
            elif name == "ABOUT QT":
                self.buttons[-1].clicked.connect(self.ABOUT_QT)

            nx = self.button_names.index(name)
            position = self.button_positions[nx]
            self.grid.addWidget(self.buttons[nx], *position)

        self.center()
        self.setFixedSize(310, 300)
        self.setWindowTitle("QHesap")
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def CLS(self):
        print("CLS")

    def BACKSPACE(self):
        print("BACKSPACE")

    def ABOUT(self):
        print("ABOUT")

    def ABOUT_QT(self):
        print("ABOUT QT")

def main(args):
    app = QApplication(args)
    qhesap = QHesap()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
