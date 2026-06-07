import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QColor, QPen, QIcon
from PySide6.QtCore import Qt, QTimer, QTime


class AnalogClock(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Analog Clock")
        self.setWindowIcon(QIcon("assets/clock.ico"))
        self.resize(600, 600)

        # Timer
        self.timer = QTimer(self)

        # Atualiza relógio a cada segundo
        self.timer.timeout.connect(self.update)

        self.timer.start(1000)

    def paintEvent(self, event):
        painter = QPainter(self)

        # Suavização
        painter.setRenderHint(QPainter.Antialiasing)

        # Fundo
        painter.fillRect(self.rect(), QColor("#0F172A"))

        # Move origem para centro
        painter.translate(self.width() / 2, self.height() / 2)

        radius = min(self.width(), self.height()) / 2 - 40

        # =========================
        # Relógio externo
        # =========================

        border_pen = QPen(QColor("#E2E8F0"))
        border_pen.setWidth(6)

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

            painter.rotate(30)

        # =========================
        # Marcações dos minutos
        # =========================

        minute_mark_pen = QPen(QColor("#475569"))
        minute_mark_pen.setWidth(2)

        painter.setPen(minute_mark_pen)

        for _ in range(60):

            if _ % 5 != 0:

                painter.drawLine(
                    0,
                    int(-radius + 25),
                    0,
                    int(-radius + 40)
                )

            painter.rotate(6)

        # =========================
        # Hora atual
        # =========================

        current_time = QTime.currentTime()

        hour = current_time.hour()
        minute = current_time.minute()
        second = current_time.second()

        # =========================
        # Ponteiro das horas
        # =========================

        painter.save()

        painter.rotate(30 * (hour + minute / 60))

        hour_hand_pen = QPen(QColor("#38BDF8"))
        hour_hand_pen.setWidth(8)

        painter.setPen(hour_hand_pen)

        glow_pen = QPen(QColor(56, 189, 248, 80))
        glow_pen.setWidth(16)

        painter.setPen(glow_pen)

        painter.setPen(hour_hand_pen)

        painter.drawLine(0, 20, 0, int(-radius * 0.5))

        painter.restore()

        # =========================
        # Ponteiro dos minutos
        # =========================

        painter.save()

        painter.rotate(6 * minute)

        minute_pen = QPen(QColor("#F8FAFC"))
        minute_pen.setWidth(6)

        glow_pen = QPen(QColor(255, 255, 255, 60))

        glow_pen.setWidth(12)

        painter.setPen(glow_pen)

        painter.setPen(minute_pen)

        painter.drawLine(0, 30, 0, int(-radius * 0.7))

        painter.restore()

        # =========================
        # Ponteiro dos segundos
        # =========================

        painter.save()

        painter.rotate(6 * second)

        second_pen = QPen(QColor("#EF4444"))
        second_pen.setWidth(3)

        painter.setPen(second_pen)

        painter.drawLine(0, 40, 0, int(-radius * 0.8))

        painter.restore()

        # =========================
        # Centro do relógio
        # =========================

        painter.setBrush(QColor("#F8FAFC"))
        painter.setPen(Qt.NoPen)

        painter.drawEllipse(-10, -10, 20, 20)

        painter.setBrush(QColor("#0F172A"))

        painter.drawEllipse(-4, -4, 8, 8)

app = QApplication(sys.argv)

window = AnalogClock()
window.show()

sys.exit(app.exec())