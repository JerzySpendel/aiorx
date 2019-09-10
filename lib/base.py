import typing


class Observable:
    async def on_subscribe(self, observer):
        pass

    def subscribe(self, observer):
        pass


class Observer:
    async def on_next(self, value):
        pass

    async def on_completed(self):
        pass

    async def on_error(self, err):
        pass


class Scheduler:
    async def schedule(self, work: typing.Coroutine):
        pass
