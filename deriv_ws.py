import websocket
import threading
import json

def iniciar_conexao(token):
    def on_open(ws):
        auth_msg = json.dumps({"authorize": token})
        ws.send(auth_msg)

    def on_message(ws, message):
        print("Mensagem recebida:", message)

    def on_error(ws, error):
        print("Erro de conexão:", error)

    def on_close(ws, *args):
        print("Conexão encerrada.")

    ws = websocket.WebSocketApp(
        "wss://ws.binaryws.com/websockets/v3?app_id=1089",
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )

    threading.Thread(target=ws.run_forever).start()