from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from random import randint


class Ui_Form(QtWidgets.QMainWindow):

    words = []
    wordToGuess = []
    usedLetters = []
    typed_text = []

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.loadWordbase()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(368, 211)
        Form.setAutoFillBackground(False)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 170, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 120, 75, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 120, 21, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 170, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 60, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Next word"))
        self.pushButton_2.setText(_translate("Form", "Submit"))
        self.pushButton_3.setText(_translate("Form", "Quit"))
        self.label.setText(_translate("Form", "Word"))
        self.pushButton_3.clicked.connect(app.quit)
        self.pushButton.clicked.connect(self.pickWord)
        self.pushButton_2.clicked.connect(self.guessLetter)

    def loadWordbase(self):
        with open("wordbase.txt", "r") as file:
            for line in file:
                line = line.strip()
                self.words.append(line)

    def pickWord(self):
        randomIndex = randint(0, len(self.words)-1)
        self.wordToGuess = self.words[randomIndex]
        self.label.setText("*" * len(self.wordToGuess))
        self.usedLetters = []

    def guessLetter(self):
        self.typed_text = self.lineEdit.text()
        self.usedLetters.append(self.typed_text)
        guessed_string = ''.join(letter if letter in self.usedLetters else '*' for letter in self.wordToGuess)
        self.label.setText(guessed_string)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())
