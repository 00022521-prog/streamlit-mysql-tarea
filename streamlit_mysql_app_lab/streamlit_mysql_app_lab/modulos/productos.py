import streamlit as st
from config.conexion import df, q
def view():
    st.header("Productos")
    st.dataframe(df("SELECT * FROM productos ORDER BY id DESC"), use_container_width=True)
    with st.form("p"):
        n = st.text_input("Nombre","")
        pr = st.number_input("Precio", 0.0, step=0.01, format="%.2f")
        s = st.number_input("Stock", 0, step=1)
        if st.form_submit_button("Guardar") and n.strip():
            q("INSERT INTO productos(nombre,precio,stock) VALUES(%s,%s,%s)",(n,pr,s)); st.rerun()
    with st.expander("Eliminar"):
        i = st.number_input("ID",1,step=1,key="prod")
        if st.button("Eliminar producto"): q("DELETE FROM productos WHERE id=%s",(int(i),)); st.rerun()
