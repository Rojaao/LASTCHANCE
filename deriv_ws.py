import websocket
import json

def iniciar_conexao(token, log_box, stake):
    def atualizar_interface(msg):
        try:
            log_box.markdown(f"```text\n{msg}\n```")
        except:
            pass

    def on_open(ws):
        auth_msg = json.dumps({ "authorize": token })
        ws.send(auth_msg)
        atualizar_interface("✅ Conexão estabelecida com a Deriv!")

    def on_message(ws, message):
        print("Mensagem recebida:", message)

    def on_error(ws, error):
        atualizar_interface(f"❌ Erro: {error}")

    def on_close(ws, close_status_code, close_msg):
        atualizar_interface("🔌 Conexão encerrada.")

    websocket.enableTrace(False)
    ws_app = websocket.WebSocketApp(
        "wss://ws.derivws.com/websockets/v3?app_id=1089",
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )

    ws_app.run_forever()
