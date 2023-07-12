from functools import cache, wraps
from asyncio import get_event_loop, AbstractEventLoop, new_event_loop


LOOP: AbstractEventLoop = new_event_loop()


from functools import cache, wraps
from typing import Awaitable, Any, Callable


class CachedAwaitable:
    def __init__(self, awaitable: Awaitable):
        self.awaitable: Awaitable = awaitable
        self.result: Any = None

    def __await__(self) -> Any:
        if not self.result:
            self.result = yield from self.awaitable.__await__()
        return self.result


def reawaitable(func: Callable, /):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return CachedAwaitable(func(*args, **kwargs))
    return wrapper


def aiocache(func: Callable, /):
    return cache(reawaitable(func))


# @cache
# @reawaitable
@aiocache
async def fibonacci(input_value):
    if input_value == 1:
        return 1
    elif input_value == 2:
        return 1
    elif input_value > 2:
        return await fibonacci(input_value - 1) + await fibonacci(input_value - 2)


async def amain():
    for i in range(1, 201):
        print(f'fib({i}) = {await fibonacci(i)}')


if __name__ == '__main__':
    LOOP.run_until_complete(amain())
