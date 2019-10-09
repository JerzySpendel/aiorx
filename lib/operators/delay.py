import asyncio

from lib.subject import ProxySubject


def delay(dt):

    class S(ProxySubject):
        async def proxy(self, value):

            async def schedule_future():
                await asyncio.sleep(dt)
                await ProxySubject.proxy(self, value)

            asyncio.ensure_future(schedule_future())

    return S()
