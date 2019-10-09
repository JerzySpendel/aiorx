from lib.subject import ProxySubject


def map(f):

    class MapOperator(ProxySubject):
        async def proxy(self, value):
            return await super().proxy(f(value))

    return MapOperator()
