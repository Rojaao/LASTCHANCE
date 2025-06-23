import streamlit as st
from deriv_ws import iniciar_conexao

def main():
    st.title("Robô Deriv - Estratégia Predador")
    token = st.text_input("Token da API", type="password")
    stake = st.number_input("Stake inicial", value=1.0)
    stop_gain = st.number_input("Stop Gain", value=10.0)
    stop_loss = st.number_input("Stop Loss", value=10.0)
    martingale = st.checkbox("Ativar Martingale")
    fator_martingale = st.number_input("Fator Martingale", value=2.0)
    status = st.empty()
    
    if st.button("Iniciar"):
        status.markdown("🔄 Iniciando conexão com a Deriv...")
        iniciar_conexao(token, stake, stop_gain, stop_loss, martingale, fator_martingale, status)