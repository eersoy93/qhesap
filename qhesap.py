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
                             QLineEdit, QMessageBox,
                             QPushButton, QWidget)

from version import QHESAP_VERSION

class QHesap(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.firstOperand = 0
        self.isPlusPressed = False
        self.isMinusPressed = False
        self.isMultiplePressed = False
        self.isDividePressed = False
        self.isEnteredFirstOperand = False

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
            elif name == "7":
                self.buttons[-1].clicked.connect(self.SEVEN)
            elif name == "8":
                self.buttons[-1].clicked.connect(self.EIGHT)
            elif name == "9":
                self.buttons[-1].clicked.connect(self.NINE)
            elif name == "/":
                self.buttons[-1].clicked.connect(self.DIVIDE)
            elif name == "4":
                self.buttons[-1].clicked.connect(self.FOUR)
            elif name == "5":
                self.buttons[-1].clicked.connect(self.FIVE)
            elif name == "6":
                self.buttons[-1].clicked.connect(self.SIX)
            elif name == "*":
                self.buttons[-1].clicked.connect(self.MULTIPLE)
            elif name == "1":
                self.buttons[-1].clicked.connect(self.ONE)
            elif name == "2":
                self.buttons[-1].clicked.connect(self.TWO)
            elif name == "3":
                self.buttons[-1].clicked.connect(self.THREE)
            elif name == "-":
                self.buttons[-1].clicked.connect(self.MINUS)
            elif name == "0":
                self.buttons[-1].clicked.connect(self.ZERO)
            elif name == ".":
                self.buttons[-1].clicked.connect(self.DECIMAL)
            elif name == "=":
                self.buttons[-1].clicked.connect(self.EQUALS)
            elif name == "+":
                self.buttons[-1].clicked.connect(self.PLUS)

            nx = self.button_names.index(name)
            position = self.button_positions[nx]
            self.grid.addWidget(self.buttons[nx], *position)

        self.center()
        self.setFixedSize(310, 300)
        self.setWindowTitle("QHesap " + QHESAP_VERSION)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def CLS(self):
        self.lineEdit.clear()

    def BACKSPACE(self):
        self.lineEdit.setText(self.lineEdit.text()[:-1])

    def ABOUT(self):
        self.aboutBox = QMessageBox.about(self,
                                          "About QHesap",
                                          "QHesap " + QHESAP_VERSION + "\n" +
                                          "Written by Erdem Ersoy (eersoy93).\n" +
                                          "Copyright (c) 2022 Erdem Ersoy\n" +
                                          "QHesap is licensed with GPLv3.\n" +
                                          "QHesap GitHub link: https://github.com/eersoy93/qhesap")

    def ABOUT_QT(self):
        self.aboutQtBox = QMessageBox.aboutQt(self, "About Qt")

    def SEVEN(self):
        NUMERAL_STR = "7"
        if not (self.isPlusPressed or self.isMinusPressed or self.isMultiplePressed or self.isDividePressed):
            self.lineEdit.setText(self.lineEdit.text() + NUMERAL_STR)
        else:
            self.lineEdit.clear()
            self.lineEdit.setText(NUMERAL_STR)

    def EIGHT(self):
        NUMERAL_STR = "8"
        if not (self.isPlusPressed or self.isMinusPressed or self.isMultiplePressed or self.isDividePressed):
            self.lineEdit.setText(self.lineEdit.text() + NUMERAL_STR)
        else:
            self.lineEdit.clear()
            self.lineEdit.setText(NUMERAL_STR)

    def NINE(self):
        NUMERAL_STR = "9"
        if not (self.isPlusPressed or self.isMinusPressed or self.isMultiplePressed or self.isDividePressed):
            self.lineEdit.setText(self.lineEdit.text() + NUMERAL_STR)
        else:
            self.lineEdit.clear()
            self.lineEdit.setText(NUMERAL_STR)

    def DIVIDE(self):
        self.isPlusPressed = False
        self.isMinusPressed = False
        self.isMultiplePressed = False
        self.isDividePressed = True

        if self.lineEdit.text() == "":
            self.firstOperand = 0.0
        else:
            try:
                self.firstOperand = float(self.lineEdit.text())
            except ValueError:
                self.lineEdit.clear(),
                self.firstOperand = 0.0

    def FOUR(self):
        NUMERAL_STR = "4"
        if not (self.isPlusPressed or self.isMinusPressed or self.isMultiplePressed or self.isDividePressed):
            self.lineEdit.setText(self.lineEdit.text() + NUMERAL_STR)
        else:
            self.lineEdit.clear()
            self.lineEdit.setText(NUMERAL_STR)

    def FIVE(self):
        NUMERAL_STR = "5"
        if not (self.isPlusPressed or self.isMinusPressed or self.isMultiplePressed or self.isDividePressed):
            self.lineEdit.setText(self.lineEdit.text() + NUMERAL_STR)
        else:
            self.lineEdit.clear()
            self.lineEdit.setText(NUMERAL_STR)

    def SIX(self):
        NUMERAL_STR = "6"
        if not (self.isPlusPressed or self.isMinusPressed or self.isMultiplePressed or self.isDividePressed):
            self.lineEdit.setText(self.lineEdit.text() + NUMERAL_STR)
        else:
            self.lineEdit.clear()
            self.lineEdit.setText(NUMERAL_STR)

    def MULTIPLE(self):
        self.isPlusPressed = False
        self.isMinusPressed = False
        self.isMultiplePressed = True
        self.isDividePressed = False

        if self.lineEdit.text() == "":
            self.firstOperand = 0.0
        else:
            try:
                self.firstOperand = float(self.lineEdit.text())
            except ValueError:
                self.lineEdit.clear(),
                self.firstOperand = 0.0

    def ONE(self):
        NUMERAL_STR = "1"
        if not (self.isPlusPressed or self.isMinusPressed or self.isMultiplePressed or self.isDividePressed):
            self.lineEdit.setText(self.lineEdit.text() + NUMERAL_STR)
        else:
            self.lineEdit.clear()
            self.lineEdit.setText(NUMERAL_STR)

    def TWO(self):
        NUMERAL_STR = "2"
        if not (self.isPlusPressed or self.isMinusPressed or self.isMultiplePressed or self.isDividePressed):
            self.lineEdit.setText(self.lineEdit.text() + NUMERAL_STR)
        else:
            self.lineEdit.clear()
            self.lineEdit.setText(NUMERAL_STR)

    def THREE(self):
        NUMERAL_STR = "3"
        if not (self.isPlusPressed or self.isMinusPressed or self.isMultiplePressed or self.isDividePressed):
            self.lineEdit.setText(self.lineEdit.text() + NUMERAL_STR)
        else:
            self.lineEdit.clear()
            self.lineEdit.setText(NUMERAL_STR)

    def MINUS(self):
        self.isPlusPressed = False
        self.isMinusPressed = True
        self.isMultiplePressed = False
        self.isDividePressed = False

        if self.lineEdit.text() == "":
            self.firstOperand = 0.0
        else:
            try:
                self.firstOperand = float(self.lineEdit.text())
            except ValueError:
                self.lineEdit.clear(),
                self.firstOperand = 0.0

    def ZERO(self):
        NUMERAL_STR = "0"
        if not (self.isPlusPressed or self.isMinusPressed or self.isMultiplePressed or self.isDividePressed):
            self.lineEdit.setText(self.lineEdit.text() + NUMERAL_STR)
        else:
            self.lineEdit.clear()
            self.lineEdit.setText(NUMERAL_STR)

    def DECIMAL(self):
        x = self.lineEdit.text()
        if x.find(".", 0, len(x)) == -1:
            self.lineEdit.setText(x + ".")

    def EQUALS(self):
        x = self.lineEdit.text()

        if self.isPlusPressed:
            self.lineEdit.setText(str(self.firstOperand + float(x)))
        elif self.isMinusPressed:
            self.lineEdit.setText(str(self.firstOperand - float(x)))
        elif self.isMultiplePressed:
            self.lineEdit.setText(str(self.firstOperand * float(x)))
        elif self.isDividePressed:
            self.lineEdit.setText(str(self.firstOperand / float(x)))

        self.isPlusPressed = False
        self.isMinusPressed = False
        self.isMultiplePressed = False
        self.isDividePressed = False

    def PLUS(self):
        self.isPlusPressed = True
        self.isMinusPressed = False
        self.isMultiplePressed = False
        self.isDividePressed = False

        if self.lineEdit.text() == "":
            self.firstOperand = 0.0
        else:
            try:
                self.firstOperand = float(self.lineEdit.text())
            except ValueError:
                self.lineEdit.clear(),
                self.firstOperand = 0.0

def main(args):
    app = QApplication(args)
    qhesap = QHesap()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
