def executar_estrategia(ticks):
    # Exemplo: entra se os três últimos dígitos forem menores que 4
    if len(ticks) >= 3 and all(int(t[-1]) < 4 for t in ticks[-3:]):
        return "PUT"
    return None