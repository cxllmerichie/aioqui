from src.aioqui.widgets import Window, Frame
from src.aioqui import asynq, CONTEXT


class App(Window):
    def __init__(self):
        super().__init__(self.__class__.__name__)
        self.setCentralWidget(Frame(self, 'qwe'))
        self.show()

    async def init(self) -> 'App':
        return self


if __name__ == '__main__':
    CONTEXT.debug = True


    async def main():
        app = App()
        # await app.init()

    asynq.run(main)

    # from PySide6.QtWidgets import QApplication
    # qapp = QApplication([])
    # app = App()
    # qapp.exec()
