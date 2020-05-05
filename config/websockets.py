import json


async def websocket_application(scope, receive, send):
    while True:
        event = await receive()

        if event["type"] == "websocket.connect":
            await send({"type": "websocket.accept"})

        if event["type"] == "websocket.disconnect":
            break

        if event["type"] == "websocket.receive":
            if event["text"] == "ping":
                await send({"type": "websocket.send", "text": "pong!"})
            if "room" in scope['path']:
                result = handle_room_command(event["text"])
                json_str = json.dumps(result)
                await send({"type": "websocket.send", "text": json_str})


def handle_room_command(text):
    return {"ok": text}
