from src.aioqui.widgets import *
from src.aioqui.asynq import asyncSlot, run

from src.aioqui import widgets


class CentralWidget(Frame):
    def __init__(self, parent: Parent):
        super().__init__(parent, self.__class__.__name__)

    async def init(self) -> 'CentralWidget':

        return self


class App(Window):
    def __init__(self):
        super().__init__(self.__class__.__name__)

    async def init(self) -> 'App':
        self.setCentralWidget(await CentralWidget(self).init())
        return self


async def main():
    app = await App().init()
    app.show()


if __name__ == '__main__':
    run(main)
