import streamlit as st, mysql.connector, pandas as pd
def conn():
    c = st.secrets["mysql"]
    return mysql.connector.connect(
        host=c["host"], port=c.get("port",3306),
        user=c["user"], password=c["password"], database=c["database"]
    )
def q(sql, params=None, fetch=False):
    con = conn(); cur = con.cursor(dictionary=True)
    cur.execute(sql, params or ())
    rows = cur.fetchall() if fetch else None
    con.commit(); cur.close(); con.close()
    return rows
def df(sql, params=None):
    return pd.DataFrame(q(sql, params, True))
