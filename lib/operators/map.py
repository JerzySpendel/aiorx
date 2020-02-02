import typing

from lib.observable import Observable
from lib.subject import ProxySubject


def map(f: typing.Callable) -> Observable:

    class MapOperator(ProxySubject):
        async def proxy(self, value):
            return await super().proxy(f(value))

    return MapOperator()
