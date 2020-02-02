import pytest

from lib.subject import ProxySubject


@pytest.mark.asyncio
async def test_proxy_subject_basic_behaviour(proxy_subject: ProxySubject):
    assert True
