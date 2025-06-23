
import streamlit as st
from deriv_ws import iniciar_conexao

def executar():
    st.set_page_config(page_title="LastChance Predador", layout="centered")
    st.title("🎯 Robô Predador Deriv")

    st.markdown("## Configurações do Robô")

    token = st.text_input("🔑 Token da API da Deriv", type="password")
    stake = st.number_input("💰 Stake Inicial", min_value=0.35, value=1.00, step=0.01)
    fator_martingale = st.number_input("📈 Fator Martingale", min_value=1.0, value=2.0, step=0.1)
    stop_gain = st.number_input("🏁 Stop Gain", min_value=1.0, value=10.0, step=0.5)
    stop_loss = st.number_input("⛔ Stop Loss", min_value=1.0, value=10.0, step=0.5)

    estrategia = st.selectbox("📊 Estratégia", ["Predador de Padrões"])
    log = st.empty()

    if st.button("🚀 Iniciar Robô"):
        if not token:
            st.warning("Por favor, insira o token da API.")
        else:
            st.success("Iniciando conexão com a Deriv...")
            iniciar_conexao(token, stake, fator_martingale, stop_gain, stop_loss, estrategia, log)
