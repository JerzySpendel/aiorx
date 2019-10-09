import types
import typing

from lib.disposable import Disposable
from lib.observer import Observer


class ObservableTools:
    @staticmethod
    def create(on_subscribe: typing.Callable[[Observer], Disposable]):
        from lib.observable import Observable

        return Observable(on_subscribe=on_subscribe)

    def pipe(self, *subjects):
        from lib.pipe import pipe

        piped = self
        for subject in subjects:
            piped = pipe(piped, subject)

        return piped

    @staticmethod
    def from_async_gen(gen):
        from lib.observable import Observable

        assert isinstance(gen, types.AsyncGeneratorType)

        class O(Observable):
            async def on_subscribe(self, observer):
                async for value in gen:
                    await observer.on_next(value)

                await observer.on_completed()

        return O()

    @staticmethod
    def from_gen(gen):
        from lib.observable import Observable

        assert isinstance(gen, types.GeneratorType)

        class O(Observable):
            async def on_subscribe(self, observer):
                for value in gen:
                    await observer.on_next(value)

                await observer.on_completed()

        return O()

    @staticmethod
    def just(value):
        from lib.observable import Observable

        class O(Observable):
            async def on_subscribe(self, observer):
                await observer.on_next(value)
                await observer.on_completed()

        return O()
