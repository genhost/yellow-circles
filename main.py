import sys
import random

from PyQt5 import uic
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow


class Circles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.do_draw = False
        self.draw_button.clicked.connect(self.draw_true)

    def draw_true(self):
        self.do_draw = True
        self.repaint()

    def paintEvent(self, _):
        if self.do_draw:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))

            d = random.randint(20, 200)

            qp.drawEllipse(300 - d // 2, 100 - d // 2, d, d)
            qp.end()
            self.do_draw = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec_())
