from lib.subject import ProxySubject


def map(f):

    class MapOperator(ProxySubject):
        async def queue_value(self, value):
            return await super().queue_value(f(value))

    return MapOperator()
