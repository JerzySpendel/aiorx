import asyncio

import pytest

from lib.observable import Observable
from lib.subject import ProxySubject


@pytest.mark.asyncio
async def test_piping(observable_12: Observable):
    """
    ProxySubject instance by default just passes everything it gets further
    so the result should be the same as without the pipe
    """
    result_box = []

    disposable = observable_12.pipe(ProxySubject()).subscribe(result_box.append)
    await disposable

    assert result_box == [1, 2]
