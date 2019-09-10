import asyncio

from lib.subject import ProxySubject


def debounce(dt):

    class S(ProxySubject):
        def __init__(self):
            super().__init__()
            self.future = None

        async def queue_value(self, value):

            async def schedule_future():
                await asyncio.sleep(dt)
                await super(S, self).queue_value(value)

            if not self.future:
                self.future = asyncio.ensure_future(schedule_future())
            else:
                self.future.cancel()
                self.future = asyncio.ensure_future(schedule_future())

    return S()
