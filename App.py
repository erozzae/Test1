import streamlit as st
from sqlalchemy import create_engine
import pandas as pd

# def connect():
#     # Initialize connection.
#     conn = st.connection('mysql', type='sql')
#     st.info("hehe")
#     Contoh query untuk mengambil data dari tabel
#     df = conn.query('SELECT * from well_a Limit 10;', ttl=600)
    
#     # Mengambil data dari database
#     for row in df.itertuples():
#         st.write(f"{row.BitDepth} has a :{row.Hkld}:")
# connect()

def connect_sql():
    connection_string = f'mysql+pymysql://{st.secrets["username"]}:{st.secrets["password"]}@{st.secrets["host"]}/{st.secrets["database"]}'
    return create_engine(connection_string)

@st.cache_data
def load_data(query):
    db_connect = connect_sql()
    result = pd.read_sql(query, db_connect)
    return result

# Main function Streamlit
def main():
    st.title("Koneksi Streamlit ke MySQL")

    query = st.text_area("Masukkan query SQL di sini:")
    if st.button("Jalankan Query"):
        data = load_data(query)
        st.write(data)

if __name__ == "__main__":
    main()