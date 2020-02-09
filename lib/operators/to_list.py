from lib.subject import ProxySubject


def to_list():
    class ToList(ProxySubject):
        def __init__(self):
            super().__init__()
            self.values = []

        async def proxy(self, value):
            self.values.append(value)

        async def on_completed(self):
            await self.proxy(self.values)
            await super().on_completed()

    return ToList()