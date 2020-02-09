import pytest


@pytest.mark.asyncio
async def test_subscribing(observable_12, event_loop):
    result_box = []

    disposable = observable_12.subscribe(result_box.append, loop=event_loop)
    await disposable

    assert result_box == [1, 2]
