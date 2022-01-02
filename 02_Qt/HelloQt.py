from PySide2 import QtWidgets

class MyQtUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Qt UI")
        self.setGeometry(300, 50, 766, 980)
        
        lWristSelectButton = QtWidgets.QPushButton("Select L_Wrist", self)
        lWristSelectButton.setGeometry(10, 10, 100, 20)
        lWristSelectButton.clicked.connect(self.onLWristSelectButtonClicked)
        
        rWristSelectButton = QtWidgets.QPushButton("Select R_Wrist", self)
        rWristSelectButton.setGeometry(120, 10, 100, 20)
        rWristSelectButton.clicked.connect(self.onRWristSelectButtonButton)

        self.show()

    def onLWristSelectButtonClicked(self):
        print("Select L_Wrist")

    def onRWristSelectButtonButton(self):
        print("Select R_Wrist")

app = QtWidgets.QApplication()
myQtUI = MyQtUI()
app.exec_()