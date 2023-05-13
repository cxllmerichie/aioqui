import functools
import asyncio
import qasync
import sys
from qasync import asyncSlot  # to import `asyncSlot` from `qasyncio`


class AsyncApp:
    @staticmethod
    def run(run_app):
        async def wrap():
            def close_future(future, loop):
                loop.call_later(10, future.cancel)
                future.cancel()

            loop = asyncio.get_event_loop()
            future = asyncio.Future()

            qapp = qasync.QApplication.instance()
            if hasattr(qapp, 'aboutToQuit'):
                getattr(qapp, 'aboutToQuit').connect(functools.partial(close_future, future, loop))

            await run_app()

            await future

        try:
            qasync.run(wrap())
        except asyncio.exceptions.CancelledError:
            sys.exit(0)
