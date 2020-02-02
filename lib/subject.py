import asyncio

from lib.event import Event
from lib.observable import Observable
from lib.observer import Observer


class Subject(Observer, Observable):
    pass


class ProxySubject(Subject):
    """
    """
    def __init__(self):
        self.queue: asyncio.Queue = asyncio.Queue()
        self.completed = False

    async def proxy(self, value):
        """
        Connection between `on_subscribe` and `on_next` methods
        """
        await self.queue.put(value)

    async def on_next(self, value):
        await self.proxy(Event(value))

    async def on_completed(self):
        await self.proxy(Event.completed())

    async def on_subscribe(self, observer: Observer):
        while True:
            event = await self.queue.get()

            if event is Event.completed():
                break

            await observer.on_next(event.value)

        await observer.on_completed()
