#The main

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, QCoreApplication
from MainWinC import MainWin
import sys

def main():
    """ Main function """
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()