import streamlit as st
from config.conexion import df, q
def view():
    st.header("Clientes")
    st.dataframe(df("SELECT * FROM clientes ORDER BY id DESC"), use_container_width=True)
    with st.form("c"):
        n = st.text_input("Nombre",""); e = st.text_input("Email",""); t = st.text_input("Teléfono","")
        if st.form_submit_button("Guardar") and n.strip():
            q("INSERT INTO clientes(nombre,email,telefono) VALUES(%s,%s,%s)",(n,e,t)); st.rerun()
    with st.expander("Eliminar"):
        i = st.number_input("ID",1,step=1)
        if st.button("Eliminar cliente"): q("DELETE FROM clientes WHERE id=%s",(int(i),)); st.rerun()
