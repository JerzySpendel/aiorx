import asyncio
from lib.action import Action
from lib.observable import Observable
from lib.observer import Observer


class Subject(Observer, Observable):
    pass


class ProxySubject(Subject):
    def __init__(self):
        self.queue: asyncio.Queue[Action] = asyncio.Queue()

    async def queue_value(self, value):
        """
        Connection between `on_subscribe` and `on_next` methods
        """
        if not isinstance(value, Action):
            value = Action(value)

        await self.queue.put(value)

    async def on_next(self, value):
        await self.queue_value(value)

    async def on_completed(self):
        await self.queue.put(Action.completed())

    async def on_subscribe(self, observer):
        while True:
            action = await self.queue.get()

            if action is Action.completed():
                break

            await observer.on_next(action.value)

        await observer.on_completed()
