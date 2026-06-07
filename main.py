import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import Qt


class AnalogClock(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Analog Clock")
        self.resize(600, 600)

    def paintEvent(self, event):
        painter = QPainter(self)

        # Suavização
        painter.setRenderHint(QPainter.Antialiasing)

        # Fundo
        painter.fillRect(self.rect(), QColor("#0F172A"))

        # Move origem para centro
        painter.translate(self.width() / 2, self.height() / 2)

        # Tamanho do relógio
        radius = min(self.width(), self.height()) / 2 - 40

        # =========================
        # Círculo externo
        # =========================

        border_pen = QPen(QColor("#E2E8F0"))
        border_pen.setWidth(4)

        painter.setPen(border_pen)

        painter.drawEllipse(
            int(-radius),
            int(-radius),
            int(radius * 2),
            int(radius * 2)
        )

        # =========================
        # Marcações das horas
        # =========================

        hour_pen = QPen(QColor("#F8FAFC"))
        hour_pen.setWidth(5)

        painter.setPen(hour_pen)

        for _ in range(12):

            painter.drawLine(
                0,
                int(-radius + 20),
                0,
                int(-radius + 50)
            )

            # Rotaciona 30 graus
            painter.rotate(30)


app = QApplication(sys.argv)

window = AnalogClock()
window.show()

sys.exit(app.exec())