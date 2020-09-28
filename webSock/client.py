#!/usr/bin/env python

import asyncio
import websockets
import time
import random

async def hello():

    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("jdfhkgjtjbkfntrjkgtrjk")
        r = await websocket.recv()
        print(r)
    # while True:
        # r = random.randint(0, 118)
        # async with websockets.connect(uri) as websocket:
            # await websocket.send(str(r))
            # a = await websocket.recv()
            # b = await websocket.recv()
            # time.sleep(1)
            # c = await websocket.recv()
            # print(f"Name: {a}  Number:{c}\n")
            # print(f"Fact: {b}\n")
# 

asyncio.get_event_loop().run_until_complete(hello())
