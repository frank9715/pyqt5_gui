import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pylupdate5 GUI")
        self.resize(640, 480)
        self.customfont = QFont('Noto Sans Mono CJK KR', 14)
        ##### Create widgets
        # self.ledPyuic = QLineEdit("venv/bin/pyuic5")
        self.ledPylupdate = QLineEdit("pylupdate5")
        self.ledPylupdate.setPlaceholderText("Location of pylupdate5 file")
        self.ledPylupdate.textChanged.connect(self.evt_change)
        self.ledPylupdate.setFont(self.customfont)

        self.ledPyFile = QLineEdit() 
        self.ledPyFile.setPlaceholderText("Input .py file")
        self.ledPyFile.textChanged.connect(self.evt_change)
        self.ledPyFile.setFont(self.customfont)

        self.ledTsFile = QLineEdit()
        self.ledTsFile.setPlaceholderText("Output .ts file")
        self.ledTsFile.textChanged.connect(self.evt_change)
        self.ledTsFile.setFont(self.customfont)

        self.chkExecutable = QCheckBox("Make executable")
        self.chkExecutable.toggled.connect(self.evt_change)
        # self.chkExecutable.setFont(self.customfont)

        self.txtCommand = QPlainTextEdit()

        self.btnpylupdate = QPushButton("...")
        self.btnpylupdate.clicked.connect(self.evt_btnPyuic_clicked)
        self.btnpylupdate.setFont(self.customfont)

        self.btnPyFile = QPushButton("...")
        self.btnPyFile.clicked.connect(self.evt_btnPyFile_clicked)
        self.btnPyFile.setFont(self.customfont)


        self.btnTsFile = QPushButton("...")
        self.btnTsFile.clicked.connect(self.evt_btnTsFile_clicked)
        self.btnTsFile.setFont(self.customfont)

        self.btnExecute = QPushButton("Execute")
        self.btnExecute.clicked.connect(self.evt_btnExecute_clicked)
        self.btnExecute.setFont(self.customfont)
        self.btnExecute.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.lytMain = QVBoxLayout()
        self.lytPyuic = QHBoxLayout()
        self.lytUIFile = QHBoxLayout()
        self.lytPyFile = QHBoxLayout()
        self.lytCommand = QHBoxLayout()

        self.lytPyuic.addWidget(self.ledPylupdate, 9)
        self.lytPyuic.addWidget(self.btnpylupdate, 1)
        self.lytMain.addLayout(self.lytPyuic)
        self.lytUIFile.addWidget(self.ledPyFile, 9)
        self.lytUIFile.addWidget(self.btnPyFile, 1)
        self.lytMain.addLayout(self.lytUIFile)
        self.lytPyFile.addWidget(self.ledTsFile, 9)
        self.lytPyFile.addWidget(self.btnTsFile, 1)
        self.lytMain.addLayout(self.lytPyFile)
        self.lytMain.addWidget(self.chkExecutable)
        self.lytCommand.addWidget(self.txtCommand, 9)
        self.lytCommand.addWidget(self.btnExecute, 1)
        self.lytMain.addLayout(self.lytCommand)

        self.setLayout(self.lytMain)

    #####  Event handlers
    def evt_btnPyuic_clicked(self):
        sFile, sExt = QFileDialog.getOpenFileName(self, "pylupdate5", os.getcwd()+"/usr/bin", "Executable Files (*)")
        if sFile:
            self.ledPylupdate.setText(sFile)

    def evt_btnPyFile_clicked(self):
        sFile, sExt = QFileDialog.getOpenFileName(self, "User Interface File", "/root/ui", "User Interface files (*.py)")
        # sFile, sExt = QFileDialog.getOpenFileName(self, "User Interface File", os.getcwd()+"/ui", "User Interface files (*.ui)")
        
        if sFile:
            self.ledPyFile.setText(sFile)
            bn = os.path.basename(sFile)
            self.ledTsFile.setText("/root/ui/"+bn.split(".")[0]+"_ko_KR.ts" + " /root/ui/"+bn.split(".")[0]+"_en_US.ts")

    def evt_btnTsFile_clicked(self):
        sFile, sExt = QFileDialog.getSaveFileName(self, "Python Module", "/root/ui", "Python Files (*.ts)")
        # sFile, sExt = QFileDialog.getSaveFileName(self, "Python Module", os.getcwd()+"/ui_modules", "Python Files (*.py)")
        if sFile:
            self.ledTsFile.setText(sFile)

    def evt_btnExecute_clicked(self):
        os.system(self.txtCommand.toPlainText())
        QMessageBox.information(self, "Execute", "You have successfully compiled {} to {}".format(self.ledPyFile.text(), self.ledTsFile.text()))

    def evt_change(self):
        if self.chkExecutable.isChecked():
            chkEx = " -x"
        else:
            chkEx = ""
        self.txtCommand.setPlainText("{}{} {} -ts {}".format(self.ledPylupdate.text(), chkEx, self.ledPyFile.text(), self.ledTsFile.text()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())