
import threading
import websocket
import json

def iniciar_conexao(token, stake, fator_martingale, stop_gain, stop_loss, estrategia, log_box):
    def atualizar_interface(msg):
        if log_box:
            log_box.markdown(f"```text\n{msg}\n```")

    def on_open(ws):
        atualizar_interface("✅ Conexão estabelecida com a Deriv!")
        auth = {
            "authorize": token
        }
        ws.send(json.dumps(auth))

    def on_message(ws, message):
        atualizar_interface("📩 Mensagem recebida: " + message)

    def on_error(ws, error):
        atualizar_interface(f"❌ Erro: {error}")

    def on_close(ws, *args):
        atualizar_interface("🔌 Conexão encerrada.")

    ws_app = websocket.WebSocketApp(
        "wss://ws.derivws.com/websockets/v3",
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )

    thread = threading.Thread(target=ws_app.run_forever)
    thread.start()
