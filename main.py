import streamlit as st
import threading
from deriv_ws import iniciar_conexao

def main():
    st.set_page_config(page_title="Robô Deriv Predador", layout="centered", page_icon="🤖")
    st.title("🤖 Robô Deriv Predador")

    token = st.text_input("Token da API", type="password")
    stake = st.number_input("Stake Inicial", value=1.0, step=0.1)
    stop_gain = st.number_input("Stop Gain", value=10.0, step=1.0)
    stop_loss = st.number_input("Stop Loss", value=10.0, step=1.0)
    fator_martingale = st.number_input("Fator Martingale", value=2.0, step=0.1)
    iniciar = st.button("Iniciar Robô")

    log = st.empty()

    if iniciar:
        log.markdown("```text\nIniciando conexão com a Deriv...\n```")
        threading.Thread(target=iniciar_conexao, args=(token, log, stake)).start()
