import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Panduan",
    page_icon="❔",
)

title_alignment="""
    <style>
    div:has(> img){
        width: 100% !important  
    }
    img{
        align-self: center
    }
    </style>
    """
st.markdown(title_alignment, unsafe_allow_html=True)

st.write("# Panduan penggunaan")


st.markdown(
    """
    Berikut adalah panduan penggunaan aplikasi web Soilmatch:
    1. Buka [https://soilmatch.parasyst.com] di browser.
"""
)


st.markdown(
    """
    2. Masukan dan sesuaikan nilai parameter di sebelah kiri sesuai dengan data yang anda miliki. Gunakan Slider dan Input Angka untuk mengatur nilai input.
"""
)
st.image(Image.open("imgs/panduan1.png"), width=400)

st.markdown(
    """
    3. Lihat hasil rekomendasi di sebelah kanan
"""
)

st.image(Image.open("imgs/panduan2.png"), width=400)

st.markdown(
    """
    4. Selesai😊
"""
)

