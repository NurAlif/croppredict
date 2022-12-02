import streamlit as st

st.set_page_config(
    page_title="Tentang Aplikasi",
    page_icon="👋", 
)

st.write("# Soilmatch 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Soil Match adalah aplikasi yang dibuat oleh kelompok 3 Goldfarb pada program Studi Independen di Orbit Future Academy. Soil Match dapat digunakan untuk memprediksi tanaman yang cocok untuk ditanam berdasarkan kriteria tanah dan lingkungan. Aplikasi ini diharapkan dapat membantu para petani dalam pengambilan keputusan dalam menentukan jenis tanaman yang akan ditanam, sehingga bisa mendapatkan hasil yang maksimal dan kerugian yang cukup besar tidak terjadi nantinya.
"""
)