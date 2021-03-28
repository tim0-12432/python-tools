import sys

from subprocess import Popen, PIPE

from PySide6.QtWidgets import *
from PySide6.QtGui import *

# https://build-system.fman.io/pyqt5-tutorial

def execute_console_command(command):
    execute = Popen(command.split(" "), stdout=PIPE)
    return execute.communicate()[0]

def file_dialog(directory='', forOpen=True, fmt='', isFolder=False):
    return QFileDialog.getExistingDirectory(self, "Select directory")

class Ui_main(QTabWidget):
    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):
        # TABS
        self.main_tab = QWidget()
        self.config_tab = QWidget()
        self.addTab(self.main_tab, "Main")
        self.addTab(self.config_tab, "Configuration")

        # TAB MAIN
        self.dir_box = QHBoxLayout()
        self.dir_box.addStretch(1)
        self.dir_btn = QPushButton("Select", self)
        self.dir_box.addWidget(self.dir_btn)

        self.main_vertical = QVBoxLayout()
        self.main_vertical.addStretch(1)
        self.main_vertical.addLayout(self.dir_box)


        # WINDOW
        self.setGeometry(50, 50, 500, 800)
        self.setWindowTitle("Git GUI+")
        #self.setWindowIcon(QIcon(""))
        self.show()

app = QApplication(sys.argv)
gui = Ui_main()
sys.exit(app.exec_())
