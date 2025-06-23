import streamlit as st
from deriv_ws import iniciar_conexao
from estrategias import predador_de_padroes

log_box = None

def atualizar_interface(msg):
    global log_box
    if log_box:
        log_box.markdown(f"```text\n{msg}\n```")

def run():
    st.set_page_config(page_title="Robô Deriv - Predador", layout="centered")
    st.title("🤖 Robô Deriv - Predador de Padrões")

    global log_box

    token = st.text_input("🎯 Token da API da Deriv", type="password")
    stake = st.number_input("💰 Stake Inicial", value=1.0)
    stop_gain = st.number_input("🟢 Stop Gain", value=10.0)
    stop_loss = st.number_input("🔴 Stop Loss", value=10.0)
    martingale = st.checkbox("🎲 Ativar Martingale", value=True)
    fator_marti = st.number_input("📈 Fator Martingale", value=2.0)
    estrategia = st.selectbox("📊 Estratégia", ["predador_de_padroes"])

    log_box = st.empty()
    if st.button("🚀 Iniciar Robô"):
        atualizar_interface("⏳ Iniciando conexão com a Deriv...")
        iniciar_conexao(token, stake, stop_gain, stop_loss, martingale, fator_marti, estrategia, atualizar_interface)
