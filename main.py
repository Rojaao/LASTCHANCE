import streamlit as st
from deriv_ws import iniciar_conexao
from estrategias.predador_de_padroes import estrategia_predador

log_box = None

def atualizar_interface(msg):
    global log_box
    if log_box:
        log_box.markdown(f"```text\n{msg}\n```")

def iniciar_app():
    global log_box
    st.set_page_config(page_title="Robô Deriv - Predador", layout="centered")
    st.title("🤖 Robô Deriv - Estratégia Predador de Padrões")

    st.subheader("Configurações do Robô")
    token = st.text_input("Token da API da Deriv", type="password")
    stake = st.number_input("Stake Inicial", min_value=0.35, value=1.00, step=0.10)
    fator_martingale = st.number_input("Fator Martingale", min_value=1.0, value=2.0, step=0.1)
    stop_loss = st.number_input("Limite de Perda (Loss)", min_value=1.0, value=10.0, step=0.5)
    stop_gain = st.number_input("Limite de Lucro (Gain)", min_value=1.0, value=20.0, step=0.5)
    usar_martingale = st.checkbox("Usar Martingale", value=True)

    if st.button("🚀 Iniciar Robô"):
        log_box = st.empty()
        atualizar_interface("🔌 Iniciando conexão com a Deriv...")
        iniciar_conexao(token, estrategia_predador, stake, fator_martingale, stop_loss, stop_gain, usar_martingale, atualizar_interface)
