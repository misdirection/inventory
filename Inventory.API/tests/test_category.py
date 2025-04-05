import asyncio
from blacksheep import Application, get
from blacksheep.testing import TestClient

app = Application()


async def test():
    # the application needs to handle its start event, to recreate a valid scenario
    await app.start()

    client = TestClient(app)

    response = await client.get("/")
    text = await response.text()

    assert response.status == 200
    assert text == "Hello, World!"

    response = await client.get("/", query={"name": "Foo"})
    text = await response.text()

    assert response.status == 200
    assert text == "Hello, Foo!"

    print("OK")


asyncio.run(test())
