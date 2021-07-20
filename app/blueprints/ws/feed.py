import asyncio
import datetime


async def feed(request, ws):

    data = await ws.recv()
    print("Received: " + data)

    while True:
        await ws.send(datetime.datetime.utcnow().isoformat())
        await asyncio.sleep(0.5)
