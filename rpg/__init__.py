import sys
from PyQt5.QtWidgets import QApplication
from rpg.mainwindow import MainWindow


def run():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
