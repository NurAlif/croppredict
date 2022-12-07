import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Tentang Aplikasi",
    page_icon="ℹ️", 
)

title_alignment="""
    <style>
    p, h3, h5, h6 {
    text-align: center
    }
    div:has(> img){
        width: 100% !important  
    }
    img{
        align-self: center
    }
    </style>
    """
st.markdown(title_alignment, unsafe_allow_html=True)


col_h1, col_h2 = st.columns([1, 3])
with col_h1:
    col_h1.image(Image.open("imgs/logo.png"), width=100)
with col_h2:
    st.write("# Soilmatch")

st.header("")

st.markdown(
    """
    Soilmatch adalah aplikasi yang dibuat oleh kelompok 3 Goldfarb pada program Studi Independen di Orbit Future Academy. Soilmatch dapat digunakan untuk memprediksi tanaman yang cocok untuk ditanam berdasarkan kriteria tanah dan lingkungan. Aplikasi ini diharapkan dapat membantu para petani dalam pengambilan keputusan dalam menentukan jenis tanaman yang akan ditanam, sehingga bisa mendapatkan hasil yang maksimal dan kerugian yang cukup besar tidak terjadi nantinya.
"""
)

st.header("")
st.header("")

col_s1, col_s2, col_s3 = st.columns(3)
with col_s1:
    col_s1.image(Image.open("imgs/mbkm.png"), width=150)
with col_s2:
    col_s2.image(Image.open("imgs/aim.png"), width=150)
with col_s3:
    col_s3.image(Image.open("imgs/orbit.jpg"), width=150)

st.header("")
st.header("")

st.markdown(
    """
    ### Pembuat
"""
)
st.write("")
st.write("")
st.write("")

col_p1, col_p2, col_p3= st.columns(3)
st.write("")
st.write("")
st.write("")
col_p4, col_p5 = st.columns(2)

with col_p1:
    st.write("##### EDA & Data Preparation")
    st.image(Image.open("imgs/alif.png"), width=150)
    st.write("##### Nur Alif Ilyasa")
    st.write("Universitas Negeri Yogyakarta")
with col_p2:
    st.write("##### Testing")
    st.image(Image.open("imgs/nanda.png"), width=150)
    st.write("##### Nanda Nafi'atul Khusna")
    st.write("Universitas Negeri Malang")
with col_p3:
    st.write("##### Deployment")
    st.image(Image.open("imgs/wiroso.png"), width=150)
    st.write("##### Wiroso")
    st.write("Universitas Dipenogoro")
with col_p4:
    st.write("##### Training & Evaluation")
    st.image(Image.open("imgs/kevin.png"), width=150)
    st.write("##### Ryan Kevin Nurhakim")
    st.write("Politeknik Harapan Bersama")
with col_p5:
    st.write("##### Training & Evaluation")
    st.image(Image.open("imgs/rian.png"), width=150)
    st.write("##### Rian Syaputra")
    st.write("Politeknik Harapan Bersama")

