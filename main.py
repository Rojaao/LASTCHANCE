import streamlit as st
from deriv_ws import iniciar_conexao

def main():
    st.title("🤖 Robô Deriv Predador")
    token = st.text_input("Token da API", type="password")
    stake = st.number_input("Stake inicial", value=1.0)
    martingale = st.checkbox("Usar Martingale", value=True)
    fator_martingale = st.number_input("Fator Martingale", value=2.0)
    stop_gain = st.number_input("Stop Gain", value=10.0)
    stop_loss = st.number_input("Stop Loss", value=10.0)

    if st.button("Iniciar"):
        st.session_state["iniciado"] = True
        st.text("🔌 Iniciando conexão com a Deriv...")
        iniciar_conexao(token)