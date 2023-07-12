from functools import cache, wraps
from asyncio import AbstractEventLoop, new_event_loop
from typing import Awaitable, Any, Callable


LOOP: AbstractEventLoop = new_event_loop()


class CachedAwaitable:
    _is_inset: str = 'CachedAwaitableResultUnset'

    def __init__(self, awaitable: Awaitable):
        self.awaitable: Awaitable = awaitable
        self.result: Any = self._is_inset

    def __await__(self) -> Any:
        if self.result == self._is_inset:
            self.result = yield from self.awaitable.__await__()
        else:
            print(self.result, self.awaitable, 'CACHED')
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


@aiocache
async def wtf(x):
    return x ** 2


async def amain():
    for i in range(1, 201):
        print(f'fib({i}) = {await fibonacci(i)}')
    print(await wtf(2))
    print(await wtf(2))
    for i in range(1, 201):
        print(f'fib({i}) = {await fibonacci(i)}')


if __name__ == '__main__':
    LOOP.run_until_complete(amain())
