import streamlit as st
from sqlalchemy import create_engine

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        # Buat koneksi menggunakan sqlalchemy create_engine
        engine = create_engine(f'mysql+mysqlconnector://{user_name}:{user_password}@{host_name}/{db_name}')
        st.info('sukses konek')
        print("Connection to MySQL DB successful")
    except Exception as e:
        print(f"The error '{e}' occurred")
    return connection



connection = create_connection(st.secrets["db_host"], st.secrets["db_username"], st.secrets["db_password"], st.secrets["db_database"])