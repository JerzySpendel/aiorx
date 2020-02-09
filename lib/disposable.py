import typing


class Disposable:
    def __init__(self, callback, await_on: typing.Optional[typing.Awaitable] = None):
        self.callback = callback
        self.await_on = await_on

    def __await__(self):
        return self.await_on.__await__()

    def dispose(self):
        self.callback()

    @classmethod
    def dummy(cls):
        return cls(callback=lambda: print("disposed"))
