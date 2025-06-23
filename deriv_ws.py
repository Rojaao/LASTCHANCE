import websocket
import threading
import json

def iniciar_conexao(token, stake, stop_gain, stop_loss, fator_martingale):
    def on_open(ws):
        ws.send(json.dumps({ "authorize": token }))

    def on_message(ws, message):
        print("Mensagem recebida:", message)

    def on_error(ws, error):
        print("Erro:", error)

    def on_close(ws, close_status_code, close_msg):
        print("Conexão encerrada.")

    ws = websocket.WebSocketApp(
        "wss://ws.binaryws.com/websockets/v3?app_id=1089",
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )

    thread = threading.Thread(target=ws.run_forever)
    thread.daemon = True
    thread.start()