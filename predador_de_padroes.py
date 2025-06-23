import json
import time

def estrategia_predador(ws, stake, fator_martingale, stop_loss, stop_gain, usar_martingale, atualizar_interface):
    atualizar_interface("📊 Estratégia Predador iniciada")
    # Exemplo mínimo de operação fake
    while True:
        proposal = {
            "buy": 1,
            "price": stake,
            "parameters": {
                "amount": stake,
                "basis": "stake",
                "contract_type": "CALL",
                "currency": "USD",
                "duration": 1,
                "duration_unit": "t",
                "symbol": "R_100"
            },
            "subscribe": 1
        }
        ws.send(json.dumps(proposal))
        atualizar_interface("🎯 Enviando proposta...")
        time.sleep(10)
