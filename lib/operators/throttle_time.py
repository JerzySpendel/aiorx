import asyncio

import typing

from lib.subject import ProxySubject


def throttle_time(dt):

    class S(ProxySubject):
        def __init__(self):
            super().__init__()
            self.accept_value = True
            self.task: typing.Optional[asyncio.Task] = None

        async def accept_again(self):
            await asyncio.sleep(dt)
            self.task = None
            self.accept_value = True

        async def queue_value(self, value):
            if self.accept_value:
                self.accept_value = False
                return await super().queue_value(value)

            if not self.task:
                self.task = asyncio.ensure_future(self.accept_again())

    return S()
