import sys
from PyQt5.QtWidgets import qApp, QLineEdit, QDialog, QProgressBar, QApplication, QWidget, QPushButton, QInputDialog, QLineEdit, QFileDialog, QMainWindow, QAction
from PyQt5.QtCore import pyqtSlot
import findwordsgenerator as fwg


class App(QMainWindow):
    input_path = ""
    output_path = ""

    def __init__(self):
        super().__init__()
        self.title = "Wordsearch"
        self.left = 50
        self.top = 50
        self.width = 400
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        btn_quit = QPushButton('Quit', self)
        btn_quit.move(200, 150)
        btn_quit.clicked.connect(QApplication.instance().quit)

        btn_add = QPushButton('Add a file', self)
        btn_add.move(200, 50)
        btn_add.clicked.connect(self.openFileNameDialog)

        btn_run = QPushButton("Run", self)
        btn_run.move(100, 150)
        btn_run.clicked.connect(self.runProgram)
        btn_run.clicked.connect(self.runProgressBar)

        btn_save = QPushButton('Save as', self)
        btn_save.move(200, 100)
        btn_save.clicked.connect(self.saveFile)

        btn_set = QPushButton('Settings', self)
        btn_set.move(100, 200)
        btn_set.clicked.connect(self.showDialog)

        self.textbox_input = QLineEdit(self)
        self.textbox_input.move(10, 50)
        self.textbox_input.resize(180, 21)

        self.textbox_output = QLineEdit(self)
        self.textbox_output.move(10, 100)
        self.textbox_output.resize(180, 21)

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(50, 250, 300, 20)

        settingAct = QAction("&Settings", self)
        fileMenu = self.menuBar().addMenu("&File")
        self.btn_set = fileMenu.addAction(settingAct)
        # self.btn_set.clicked.connect(self.showDialog)

        # self.le = QLineEdit(self)
        # self.le.move(130, 22)

        self.show()

    @pyqtSlot()
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "C:/Users/agata/AppData/Local/Programs/Python/Python36-32/games/wordsearch", "All Files (*);;Text Files (*.txt)", options=options)
        if file:
            self.input_path = file
            self.textbox_input.setText(file)
            print("wybrano plik", file)

    def saveFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(
            self, "QFileDialog.getSaveFileName()", "", "Text Files (*.pdf)", options=options)
        if fileName:
            self.output_path = fileName
            self.textbox_output.setText(fileName)
            print("wybrano plik", fileName)

    def runProgram(self):
        if self.input_path != "" and self.output_path != "":
            fwg.words_generator(
                self.input_path, self.output_path, self.w)

    def runProgressBar(self):
        if self.input_path != "" and self.output_path != "":
            self.completed = 0
            while self.completed < 100:
                self.completed += 0.0001
                self.pbar.setValue(self.completed)

    def showDialog(self):
        int, ok = QInputDialog.getInt(self, 'Input Dialog', 'Set table size')
        if ok and int != 0:
            self.w = int


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
