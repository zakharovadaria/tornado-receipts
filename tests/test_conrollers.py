import pytest


@pytest.mark.gen_test
async def test_base_get(http_client, base_url):
    response = await http_client.fetch(base_url)

    assert response.body == b"Hello, world!"
