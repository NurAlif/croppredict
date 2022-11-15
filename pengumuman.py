import streamlit as st
import pandas as pd
import json

title_alignment="""
    <style>
    h1, h3, h6 {
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

nim = st.text_input("Masukan NIM : ")

dataraw = json.load(open("finalis.json"))
df = pd.DataFrame(data=dataraw["finalis"])

if nim != "":

    diterima = None
    mhs = ""
    for x in dataraw["finalis"]:
        if x["NIM"] == nim:
            mhs = x["nama"]
            diterima = 1
    if diterima == None:
        data = 0
        for x in dataraw["pendaftar"]:
            if x['NIM'] == nim :
                data = 1
                mhs = x["nama"]
                st.header("Maaf untuk saat ini belum diterima. Semangat dan selamat mencoba lagi di tahun depan.. Tetap semangat!")
                st.write("Nama : "+mhs)
                break
        if data == 0:
            st.header("Data tidak ditemukan!")

    else:
        st.title("Selamat anda diterima!")
        st.write("Nama : "+mhs)
    
