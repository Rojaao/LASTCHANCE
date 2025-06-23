import websocket
import json
import threading

log_box = None

def iniciar_conexao(token, estrategia_func, stake, fator_martingale, stop_loss, stop_gain, usar_martingale, atualizar_interface):
    def on_open(ws):
        auth_msg = json.dumps({ "authorize": token })
        ws.send(auth_msg)

    def on_message(ws, message):
        data = json.loads(message)
        print("📩", data)
        if 'error' in data:
            atualizar_interface(f"❌ Erro: {data['error']['message']}")
            return
        if data.get("msg_type") == "authorize":
            atualizar_interface("✅ Conectado com sucesso à Deriv!")
            threading.Thread(target=estrategia_func, args=(ws, stake, fator_martingale, stop_loss, stop_gain, usar_martingale, atualizar_interface), daemon=True).start()

    def on_error(ws, error):
        atualizar_interface(f"❌ Erro: {error}")

    def on_close(ws, close_status_code, close_msg):
        atualizar_interface("🔌 Conexão encerrada.")

    ws_app = websocket.WebSocketApp("wss://ws.derivws.com/websockets/v3?app_id=1089",
                                     on_open=on_open,
                                     on_message=on_message,
                                     on_error=on_error,
                                     on_close=on_close)

    threading.Thread(target=ws_app.run_forever, daemon=True).start()
