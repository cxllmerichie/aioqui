from src.aioqui.widgets import *
from src.aioqui.qasyncio import AsyncApp, asyncSlot
from src.aioqui import CONTEXT, qasyncio


css = f'''
#CentralWidget {{
    background-color: yellow;
}}

#ElideLeftLbl,
#ElideRightLbl {{
    background-color: blue;
}} 
'''


class CentralWidget(Frame):
    def __init__(self, parent: Parent):
        super().__init__(parent, self.__class__.__name__, stylesheet=css)

    async def init(self) -> 'CentralWidget':
        self.setLayout(await Layout.vertical().init(
            spacing=5, alignment=Layout.Center, margins=(5, 5, 5, 5),
            items=[
                await Frame(self, 'ElidedLabelsFrame').init(
                    layout=await Layout.vertical().init(
                        spacing=50,
                        items=[
                            await Label(self, 'ElideLeftLbl').init(
                                text='Elide left', elide=Label.ElideLeft,
                                sizes=Label.Sizes(
                                    min_width=100
                                )
                            ), Layout.Left,
                            await Label(self, 'ElideRightLbl').init(
                                text='Elide right', elide=Label.ElideRight
                            ), Layout.Right
                        ]
                    )
                ),
                await Button(self, 'TestBtn').init(
                    events=Button.Events(
                        on_click=self.test
                    )
                )
            ]
        ))
        return self

    @asyncSlot()
    async def test(self):
        print('oh')


class App(Window):
    def __init__(self):
        super().__init__(self.__class__.__name__)

    async def init(self) -> 'App':
        self.setCentralWidget(await CentralWidget(self).init())
        return self


if __name__ == '__main__':
    async def run_app():
        app = await App().init()
        app.show()

    AsyncApp.run(run_app)
