import streamlit as st
from sqlalchemy import create_engine
import pandas as pd


def connect_sql():
    connection_string = f'mysql+pymysql://{st.secrets["username"]}:{st.secrets["password"]}@{st.secrets["host"]}:{st.secrets["port"]}/{st.secrets["database"]}'
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