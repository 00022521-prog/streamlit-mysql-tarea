import streamlit as st, hashlib
from config.conexion import q
def h(p): return hashlib.sha256(p.encode()).hexdigest()
def view():
    st.subheader("Inicio de sesión")
    u = st.text_input("Usuario"); p = st.text_input("Contraseña", type="password")
    c1, c2 = st.columns(2)
    if c1.button("Entrar"):
        r = q("SELECT id,username,rol FROM usuarios WHERE username=%s AND password_hash=%s",(u,h(p)),True)
        if r:
            st.session_state.update(logged=True, uid=r[0]['id'], user=r[0]['username'], rol=r[0]['rol'])
            st.success("¡Bienvenido!") st.rerun()
        else: st.error("Credenciales inválidas")
    if c2.button("Crear usuario demo (admin/admin)"):
        q("INSERT IGNORE INTO usuarios(username,password_hash,rol) VALUES('admin',%s,'admin')",(h('admin'),))
        st.success("Usuario demo listo")
