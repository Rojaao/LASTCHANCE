def executar_estrategia(ticks):
    # Exemplo: entra se os dois últimos dígitos forem maiores que 5
    if len(ticks) >= 2 and int(ticks[-1][-1]) > 5 and int(ticks[-2][-1]) > 5:
        return "CALL"
    return None
