import json
import time

def predador_de_padroes(ws, stake, stop_gain, stop_loss, martingale, fator_marti, atualizar_interface):
    saldo = 0
    perda_acumulada = 0
    ganho_acumulado = 0
    entrada_atual = stake

    def enviar_ordem():
        contrato = {
            "buy": 1,
            "price": entrada_atual,
            "parameters": {
                "amount": entrada_atual,
                "basis": "stake",
                "contract_type": "CALL",
                "currency": "USD",
                "duration": 1,
                "duration_unit": "t",
                "symbol": "R_100"
            },
            "passthrough": {},
            "req_id": 1
        }
        ws.send(json.dumps(contrato))
        atualizar_interface(f"🎯 Ordem enviada: ${entrada_atual}")

    def on_message(ws_inner, message):
        nonlocal entrada_atual, ganho_acumulado, perda_acumulada
        data = json.loads(message)
        if "error" in data:
            atualizar_interface("❌ Erro na resposta: " + data["error"]["message"])
            return
        if "profit" in data.get("buy", {}):
            lucro = float(data["buy"]["profit"])
            if lucro > 0:
                ganho_acumulado += lucro
                perda_acumulada = 0
                entrada_atual = stake
                atualizar_interface(f"✅ WIN: +{lucro:.2f}")
            else:
                perda_acumulada += abs(lucro)
                if martingale:
                    entrada_atual *= fator_marti
                atualizar_interface(f"❌ LOSS: {lucro:.2f}")
            if ganho_acumulado >= stop_gain or perda_acumulada >= stop_loss:
                atualizar_interface("🎯 Meta atingida. Robô parado.")
            else:
                time.sleep(2)
                enviar_ordem()

    ws.on_message = on_message
    enviar_ordem()
