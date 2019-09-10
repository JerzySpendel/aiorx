import typing


class Scheduler:
    async def schedule(self, work: typing.Coroutine):
        pass


class SimpleScheduler(Scheduler):
    async def schedule(self, work: typing.Coroutine):
        return await work
