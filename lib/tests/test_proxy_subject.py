import asyncio

import pytest

from lib.event import Event
from lib.observer import Observer
from lib.subject import ProxySubject


@pytest.fixture()
def proxy_subject() -> ProxySubject:

    class ExampleProxySubject(ProxySubject):
        pass

    return ExampleProxySubject()


@pytest.fixture()
def event_loop():
    return asyncio.get_event_loop()


@pytest.mark.asyncio
async def test_proxy_subject_basic_behaviour(proxy_subject: ProxySubject, event_loop):
    """
    Testing that subject accepts anything in their ProxySubject.proxy method and
    passes it to the observer.

    Here we have start_pushing() coroutine that sends two values to the subject.
    We subscribe consumer() to the subject and test that after everything the `values` list
    has 2 items
    """
    value = 'some value'
    values = []

    async def start_pushing():
        await asyncio.sleep(.1)
        await proxy_subject.proxy(Event(value))
        await asyncio.sleep(.1)
        await proxy_subject.proxy(Event(value))

    async def consumer(value):
        values.append(value)

    disposable = proxy_subject.subscribe(Observer.from_async(consumer), loop=event_loop)
    handler = asyncio.ensure_future(start_pushing())
    await handler
    disposable.dispose()

    assert len(values) == 2

