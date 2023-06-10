from src.aioqui.widgets import *
from src.aioqui.asynq import asyncSlot, run


class CentralWidget(Frame):
    def __init__(self, parent: Parent):
        super().__init__(parent, self.__class__.__name__)

    async def init(self) -> 'CentralWidget':
        from src.aioqui.widgets.custom import DurationLabel
        self.setLayout(await Layout.vertical(self).init(
            margins=(50, 50, 50, 50),
            items=[
                await Button(self, 'Btn').init(
                    on_click=lambda: self.Lbl.setText('Temporary text')
                ),
                await DurationLabel(self, 'Lbl').init(

                ),
                await Input.line(self, 'LInp1').init(
                    placeholder='hello there'
                ),
                await Input.line(self, 'LInp2').init(
                    placeholder='hello there'
                )
            ]
        ))
        self.LInp1.setPlaceholderText('color: black;')
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
