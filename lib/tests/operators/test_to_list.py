import pytest

from lib.observable import Observable
from lib.observer import Observer
from lib.operators import to_list


@pytest.fixture()
def observable():
    class SomeObservable(Observable):
        async def on_subscribe(self, observer: Observer):
            await observer.on_next(1)
            await observer.on_next(2)
            await observer.on_next(3)

    return SomeObservable()


@pytest.mark.asyncio
async def test_to_list_operator(observable: Observable, event_loop):
    result_box = []

    disposable = observable.pipe(to_list()).subscribe(result_box.append, loop=event_loop)

    await disposable

