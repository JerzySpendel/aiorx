import typing

from lib.base import Observer, Observable
from lib.subject import ProxySubject


def merge(*obs: Observable):

    class S(ProxySubject):
        def __init__(self):
            super().__init__()
            self.completes_counter = 0

        async def on_completed(self):
            if self.completes_counter < len(obs):
                self.completes_counter += 1
            else:
                return await super().on_completed()

        async def on_subscribe(self, observer: Observer):
            for observable in obs:
                observable.subscribe(self)

            return await super().on_subscribe(observer)

    return S()
