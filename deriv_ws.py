
import websocket, json

def iniciar_conexao(token):
    def on_open(ws):
        ws.send(json.dumps({"authorize": token}))

    ws = websocket.WebSocketApp(
        "wss://ws.derivws.com/websockets/v3?app_id=1089",
        on_open=on_open
    )
    ws.run_forever()
