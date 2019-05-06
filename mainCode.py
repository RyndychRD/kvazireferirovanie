import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QLabel, QMainWindow
from PyQt5 import uic
import Abstractor.startAbstr as startAbstr

#main class
class extractiveSummarization(QMainWindow):

#same as onCreate
    def __init__(self):
        super().__init__()
        uic.loadUi('window.ui', self)
        #attaching function to button
        self.doRefer.clicked.connect(self.retrieveText)


#function attached to button
    def retrieveText(self):
        words = self.textInput.toPlainText()
        number = self.numberBox.value()
        words = startAbstr.startAbstraction(words,float(number/100))
        self.textOutput.setText(words)

app = QApplication(sys.argv)
widget = extractiveSummarization()
widget.show()

sys.exit(app.exec_())
