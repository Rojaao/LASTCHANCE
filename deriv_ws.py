import websocket, json, threading

def iniciar_conexao(token, stake, stop_gain, stop_loss, martingale, fator_martingale, status_display):
    def on_open(ws):
        status_display.markdown("✅ Conexão estabelecida com a Deriv!")
        auth_msg = json.dumps({ "authorize": token })
        ws.send(auth_msg)

    def on_message(ws, message):
        print(f"Mensagem recebida: {message}")

    def on_error(ws, error):
        status_display.markdown(f"❌ Erro: {error}")

    def on_close(ws, close_status_code, close_msg):
        status_display.markdown("🔌 Conexão encerrada.")

    ws = websocket.WebSocketApp(
        "wss://ws.derivws.com/websockets/v3?app_id=1089",
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )
    threading.Thread(target=ws.run_forever).start()