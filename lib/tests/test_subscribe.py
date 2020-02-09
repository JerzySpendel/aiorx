import pytest

from lib.observable import Observable
from lib.observer import Observer


@pytest.fixture()
def observable():
    class SomeObservable(Observable):
        async def on_subscribe(self, observer: Observer):
            await observer.on_next(1)
            await observer.on_next(2)

    return SomeObservable()


@pytest.mark.asyncio
async def test_subscribing(observable, event_loop):
    result_box = []

    disposable = observable.subscribe(result_box.append, loop=event_loop)
    await disposable

    assert result_box == [1, 2]
