from PyQt6.QtWidgets import QApplication, QHBoxLayout, QWidget, QPushButton
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDrag
import sys


class DragButton(QPushButton):

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)
            drag.exec(Qt.MoveAction)

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.blayout = QHBoxLayout()
        for l in ['A', 'B', 'C', 'D']:
            btn = DragButton(l)
            self.blayout.addWidget(btn)

        self.setLayout(self.blayout)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        pos = e.pos()
        widget = e.source()

        for n in range(self.blayout.count()):
            w = self.blayout.itemAt(n).widget()
            if pos.x() < w.x() + w.size().width // 2:
                self.blayout.insertWidget(n-1, widget)
                break

        e.accept()

app = QApplication([])
window = Window()
window.show()

sys.exit(app.exec())