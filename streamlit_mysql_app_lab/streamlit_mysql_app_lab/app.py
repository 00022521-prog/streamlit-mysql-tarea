import streamlit as st
from modulos.login import view as login_view
from modulos.clientes import view as clientes_view
from modulos.productos import view as productos_view
from modulos.ventas import view as ventas_view

st.set_page_config(page_title="App Streamlit + MySQL", page_icon="🗄️", layout="wide")

def menu():
    with st.sidebar:
        st.header("Menú")
        return st.radio("Secciones", ["Clientes","Productos","Ventas"])

if not st.session_state.get("logged"):
    login_view()
else:
    with st.sidebar:
        st.caption(f"Usuario: {st.session_state.get('user','')}")
        if st.button("Cerrar sesión"):
            st.session_state.clear(); st.experimental_rerun()
    s = menu()
    {"Clientes": clientes_view, "Productos": productos_view, "Ventas": ventas_view}[s]()
