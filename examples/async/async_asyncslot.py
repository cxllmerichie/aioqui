# last update far ago


"""Display LCD-style digital clock"""

import asyncio
import datetime
import qtinter  # <-- import module
from PySide6.QtWidgets import QWidget, QLCDNumber, QVBoxLayout, QPushButton, QApplication


class Window(QWidget):
    def __init__(self):
        super().__init__()

    def init(self):
        layout = QVBoxLayout()

        clock = Clock()
        self.clock = clock
        clock.setWindowTitle("qtinter - Digital Clock example")
        clock.resize(300, 50)
        layout.addWidget(clock)

        btn = QPushButton(self)
        btn.clicked.connect(qtinter.asyncslot(self.hm))
        btn.setText('Zhopa')
        layout.addWidget(btn)

        self.setLayout(layout)
        return self

    async def hm(self):
        print('test')

    def show(self) -> None:
        super().show()
        self.clock.show()


class Clock(QLCDNumber):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDigitCount(8)

    def showEvent(self, event):
        self._task = asyncio.create_task(self._tick())

    def hideEvent(self, event):
        self._task.cancel()

    async def _tick(self):
        while True:
            t = datetime.datetime.now()
            self.display(t.strftime("%H:%M:%S"))
            await asyncio.sleep(1.0 - t.microsecond / 1000000 + 0.05)


if __name__ == "__main__":
    qapp = QApplication([])
    with qtinter.using_asyncio_from_qt():  # <-- enable asyncio in qt code
        app = Window().init()
        app.show()
        qapp.exec()
