import asyncio

import typing

from lib.subject import ProxySubject


def throttle_time(dt):

    class S(ProxySubject):
        def __init__(self):
            super().__init__()
            self.accepting_values = True
            self.task: typing.Optional[asyncio.Task] = None

        async def start_accepting(self):
            await asyncio.sleep(dt)
            self.task = None
            self.accepting_values = True

        async def queue_value(self, value):
            if self.accepting_values:
                self.accepting_values = False
                return await super().queue_value(value)

            if not self.task:
                self.task = asyncio.ensure_future(self.start_accepting())

    return S()
