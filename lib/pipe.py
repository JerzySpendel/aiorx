from lib.subject import Subject, ProxySubject
from lib.observer import Observer


def pipe(source: Subject, output: Subject) -> Subject:
    class S(Subject):
        async def on_next(self, value):
            await source.on_next(value)

        def subscribe(self, observer: Observer):
            source.subscribe(output)
            output.subscribe(observer)

    return S()
