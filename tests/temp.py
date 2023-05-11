from PyQt5.QtWidgets import QWidget

from src.qcontext.widgets import Window, Frame, Layout, Button, Label
from src.qcontext.qasyncio import AsyncApp
from src.qcontext import CONTEXT, qasyncio


async def async_func():
    print('Async func called')


class CentralWidget(Frame):
    def __init__(self, parent: QWidget):
        super().__init__(parent, self.__class__.__name__)

    async def init(self) -> 'CentralWidget':
        self.setLayout(await Layout.vertical().init(
            spacing=5, alignment=Layout.Center, margins=(5, 5, 5, 5),
            items=[
                await Label(self, 'TextLbl').init(
                    text='Some' + ' long' * 10 + 'text', wrap=True, alignment=Label.TopCenter
                ),
                await Layout.horizontal().init(
                    items=[
                        await Button(self, 'TestBtn1').init(
                            slot=self.test_context_global, text='Test `CONTEXT`'
                        ),
                        await Button(self, 'TestBtn2').init(
                            slot=self.test_context_self, text='Test `CONTEXT`'
                        )
                    ]
                )
            ]
        ))
        return self

    @qasyncio.asyncSlot()
    async def test_context_global(self):
        CONTEXT.TextLbl.setText('Text was set using `CONTEXT`')
        await async_func()

    @qasyncio.asyncSlot()
    async def test_context_self(self):
        self.TextLbl.setText('Text was set using `self`')
        await async_func()


class App(Window):
    def __init__(self):
        super().__init__(self.__class__.__name__)

    async def init(self) -> 'App':
        self.setCentralWidget(await CentralWidget(self).init())
        return self


if __name__ == '__main__':
    async def run_app():
        async with AsyncApp():
            (await App().init()).show()

    AsyncApp.run(run_app)
