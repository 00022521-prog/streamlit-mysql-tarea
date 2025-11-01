import streamlit as st
from config.conexion import df, q
def view():
    st.header("Ventas")
    cl = df("SELECT id,nombre FROM clientes ORDER BY nombre")
    pr = df("SELECT id,nombre,precio FROM productos ORDER BY nombre")
    with st.form("v"):
        c = st.selectbox("Cliente", cl["id"].tolist() if not cl.empty else [], 
                         format_func=lambda i: cl.set_index("id").loc[i,"nombre"] if not cl.empty else str(i))
        p = st.selectbox("Producto", pr["id"].tolist() if not pr.empty else [],
                         format_func=lambda i: pr.set_index("id").loc[i,"nombre"] if not pr.empty else str(i))
        cant = st.number_input("Cantidad",1,step=1,value=1)
        if st.form_submit_button("Registrar"):
            if cl.empty or pr.empty: st.warning("Agrega clientes y productos primero.")
            else:
                precio = float(pr.set_index("id").loc[p,"precio"])
                q("INSERT INTO ventas(cliente_id,producto_id,cantidad,total) VALUES(%s,%s,%s,%s)",(c,p,cant,precio*cant))
                st.experimental_rerun()
    st.dataframe(df("""SELECT v.id, c.nombre cliente, p.nombre producto, v.cantidad, v.total, v.fecha
                       FROM ventas v LEFT JOIN clientes c ON c.id=v.cliente_id
                       LEFT JOIN productos p ON p.id=v.producto_id
                       ORDER BY v.id DESC"""), use_container_width=True)
