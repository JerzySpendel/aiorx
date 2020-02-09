import pytest

from lib.observable import Observable
from lib.observer import Observer


@pytest.fixture()
def observable_12():
    class SomeObservable(Observable):
        async def on_subscribe(self, observer: Observer):
            await observer.on_next(1)
            await observer.on_next(2)

    return SomeObservable()