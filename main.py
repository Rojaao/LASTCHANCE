import streamlit as st
from deriv_ws import iniciar_conexao

def main():
    st.set_page_config(page_title="Robô Predador Deriv", layout="centered")
    st.title("🤖 Robô Predador Deriv")

    token = st.text_input("Token da API", type="password")
    stake = st.number_input("Stake inicial", value=1.0)
    stop_gain = st.number_input("Stop Gain", value=10.0)
    stop_loss = st.number_input("Stop Loss", value=10.0)
    fator_martingale = st.number_input("Fator Martingale", value=2.0)

    if st.button("Iniciar Robô"):
        if token:
            st.success("Iniciando conexão com a Deriv...")
            iniciar_conexao(token, stake, stop_gain, stop_loss, fator_martingale)
        else:
            st.error("Informe um token válido.")

if __name__ == "__main__":
    main()