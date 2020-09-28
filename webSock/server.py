import asyncio
import websockets


async def numberGet(websocket, path):
    edancho = await websocket.recv()
    if "PISHKA" in str(edancho):
        await websocket.send("mangasar")
    elif "PUTKA" in str(edancho):
        print("haha")
    else:
        await websocket.send("greshen otgovor")
        # d = mendeleev.get_all_elements()
        # gei = await websocket.recv()
        # print(gei)
        # a = d[int(gei)]
        # await websocket.send(a.name)
        # await websocket.send(a.uses)
        # await websocket.send(str(a.atomic_number))

start_server = websockets.serve(numberGet, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
