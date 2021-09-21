#The MainWindow

from PyQt5.QtWidgets import QMainWindow
from Ui_main_win import Ui_MainWindow
from HelpWinC import HelpWin

class MainWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """ Main Window class"""
        super(MainWin, self).__init__()
        self.setupUi(self)
        self.help_win = HelpWin(self)
        self.Retry_Btn.clicked.connect(self.board.retry)

    def help(self):
        """ Help function """
        self.help_win.show()
