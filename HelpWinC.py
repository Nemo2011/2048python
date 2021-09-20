#The help window

from PyQt5.QtWidgets import QWidget
from Ui_help import Ui_Form

class HelpWin(QWidget, Ui_Form):
    def __init__(self, parent=None):
        """ Help Window class"""
        super(HelpWin, self).__init__()
        self.setupUi(self)