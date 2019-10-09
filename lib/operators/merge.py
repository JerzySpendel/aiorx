import typing

from lib.base import Observer, Observable
from lib.subject import ProxySubject


def merge(*obs: Observable):
    class S(ProxySubject):
        async def on_subscribe(self, observer: Observer):
            for observable in obs:
                observable.subscribe(self)

            return await super().on_subscribe(observer)

    return S()
