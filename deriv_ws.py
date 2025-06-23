import websocket
import threading
import json
from estrategias import predador_de_padroes

def iniciar_conexao(token, stake, stop_gain, stop_loss, martingale, fator_marti, estrategia_nome, atualizar_interface):
    def on_open(ws):
        ws.send(json.dumps({"authorize": token}))
        atualizar_interface("✅ Conexão estabelecida com a Deriv!")

        if estrategia_nome == "predador_de_padroes":
            predador_de_padroes(ws, stake, stop_gain, stop_loss, martingale, fator_marti, atualizar_interface)

    def on_error(ws, error):
        atualizar_interface(f"❌ Erro: {error}")

    def on_close(ws, close_status_code, close_msg):
        atualizar_interface("🔌 Conexão encerrada.")

    ws_app = websocket.WebSocketApp(
        "wss://ws.derivws.com/websockets/v3?app_id=1089",
        on_open=on_open,
        on_error=on_error,
        on_close=on_close,
    )
    thread = threading.Thread(target=ws_app.run_forever)
    thread.start()
