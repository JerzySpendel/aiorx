from lib.subject import ProxySubject


def first():
    class S(ProxySubject):
        async def queue_value(self, value):
            await super().proxy(value)

    return S()
