import streamlit as st
from sqlalchemy import create_engine


def connect():
    # Initialize connection.
    conn = st.connection('mysql', type='sql')
    # Contoh query untuk mengambil data dari tabel
    df = conn.query('SELECT * from well_a Limit 10;', ttl=600)
    
    # Mengambil data dari database
    for row in df.itertuples():
        st.write(f"{row.BitDepth} has a :{row.Hkld}:")
connect()