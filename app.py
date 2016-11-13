import sys
import util

from PyQt5.QtWidgets import (QWidget, QDesktopWidget, QScrollArea, QDialog, QComboBox, QPushButton, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        modulas = QLabel('n =')
        bitA = QLabel('Bits of A:')
        bitB = QLabel('Bits of B:')
        numA = QLabel('A =')
        numB = QLabel('B =')
        res = QLabel('A^B mod n =')
        realRes = QLabel('Real result =')
        
        self.numA = QLabel('')
        self.numB = QLabel('')
        self.res = QLabel('')
        self.realRes = QLabel('')

        self.modulasEdit = QLineEdit()

        self.cbA = QComboBox()
        self.cbB = QComboBox()
        list = ['8', '16', '32', '64']
        self.cbA.addItems(list)
        self.cbB.addItems(list)

        btn1 = QPushButton('Generate && Calculate', self)
        btn1.clicked.connect(self.buttonClicked)
        btn2 = QPushButton('Try to print A^B', self)
        btn2.clicked.connect(self.print)
        
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(modulas, 1, 0)
        grid.addWidget(self.modulasEdit, 1, 1)
        grid.addWidget(bitA, 2, 0)
        grid.addWidget(self.cbA, 2, 1)
        grid.addWidget(bitB, 3, 0)
        grid.addWidget(self.cbB, 3, 1)

        grid.addWidget(btn1, 4, 0, 1, 2)
        grid.addWidget(numA, 5, 0)
        grid.addWidget(self.numA, 5, 1)
        grid.addWidget(numB, 6, 0)
        grid.addWidget(self.numB, 6, 1)
        grid.addWidget(res, 7, 0)
        grid.addWidget(self.res, 7, 1)
        grid.addWidget(realRes, 8, 0)
        grid.addWidget(self.realRes, 8, 1)
        grid.addWidget(btn2, 9, 0, 1, 2)

        self.setLayout(grid)

        self.setWindowTitle('a^b mod n')
        self.move(
            QDesktopWidget().availableGeometry().center() -
            self.frameGeometry().center()
        )
        self.show()

    def buttonClicked(self):
        bitsOfA = int(self.cbA.currentText())
        bitsOfB = int(self.cbB.currentText())
        a = util.test(util.makeOdd(util.randomString(bitsOfA)))
        self.numA.setText(str(a))
        b = util.test(util.makeOdd(util.randomString(bitsOfB)))
        self.numB.setText(str(b))
        n = int(self.modulasEdit.text())
        res = util.powMod(a, b, n, True)
        self.res.setText(str(res))
        self.realRes.setText(str(a**b%n))
        
    def print(self):
        a = int(self.numA.text())
        b = int(self.numB.text())
        res = util.powMod(a, b, 10, False)
        d = QDialog()
        label = QTextEdit('', d)
        label.setText(str(res))

        grid = QGridLayout(d)
        grid.setSpacing(10)

        grid.addWidget(label, 1, 0, 1, 2)
        d.setWindowTitle('Printed result')
        d.exec_()
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
