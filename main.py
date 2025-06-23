
import streamlit as st
import threading
from deriv_ws import iniciar_conexao

def main():
    st.title("Robô Deriv Predador")
    token = st.text_input("Token da API")
    if st.button("Iniciar"):
        st.write("Iniciando conexão...")
        threading.Thread(target=iniciar_conexao, args=(token,)).start()
