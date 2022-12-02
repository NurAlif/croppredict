import streamlit as st

st.set_page_config(
    page_title="Panduan",
    page_icon="👋",
)

st.write("# Panduan penggunaan 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Berikut adalah panduan penggunaan aplikasi web Soilmatch:
    1. Buka [http://soilmatch.eastasia.cloudapp.azure.com:8501] dan pilih ke halaman deteksi.
    2. Masukan dan sesuaikan nilai parameter di sebelah kiri sesuai dengan data yang anda miliki. 
    3. Lihat hasil rekomendasi
"""
)