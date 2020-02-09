from lib.subject import Subject, ProxySubject
from lib.observer import Observer


def pipe(source: Subject, output: Subject) -> Subject:
    class S(Subject):
        async def on_next(self, value):
            await source.on_next(value)

        def subscribe(self, observer: Observer, loop=None):
            output.subscribe(observer, loop)
            return source.subscribe(output, loop)

    return S()
