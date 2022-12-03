import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd
import json
from PIL import Image

st.set_page_config(
    page_title="Rekomendasi tanaman",
    page_icon="🌱",
)

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

crops = json.load(open("crops.json"))

labels = crops["labels"]
imgs = crops['imgs']
descs = crops['desc']

class_len = 22


loaded_model = tf.keras.models.load_model("lstm.h5")


def analyze(input_data):
    input_data = input_data.reshape(1, 7, 1)
    pred = loaded_model.predict(input_data)
    return pred[0]

input_values = np.zeros(7)



st.image(Image.open("logo.png"), width=150)
st.title("Rekomendasi Tanaman Soilmatch")
col1, col2 = st.columns(2)

with col1:
    st.button('❔Bantuan')
    input_values[0] = st.slider('Kandungan nitrogen dalam tanah (%)', .0, 100.0, value=90.0)
    input_values[1] = st.slider('Kandungan fosfor dalam tanah (%)', .0, 100.0, value=42.5)
    input_values[2] = st.slider('Kandungan potasium dalam tanah (%)', .0, 100.0, value=43.4)
    input_values[3] = st.number_input('Temperatur udara(°C)', value=20.2)
    input_values[4] = st.number_input('Kelembapan udara (%)', value=82.5)
    input_values[5] = st.number_input('Kandungan Asam (Ph)', value=6.5)
    input_values[6] = st.number_input('Intensitas Hujan (mm)', value=200.9)

with col2:
    new_title = """
    <div style="border-style: solid;padding: 10px;border-radius: 10px;border-width: 1px;margin: 10px;">
        <h6> Sesuaikan parameter masukan! </h6>
        <p style="text-align: center; text-size: "> Keluaran akan otomatis menyesuaikan ketika parameter dirubah </p>
    </div>
    """

    st.markdown(new_title, unsafe_allow_html=True)
    st.header("")
    st.header("")
    with st.spinner('Tunggu sebentar...'):
        result = analyze(input_values)
        idx = np.argmax(result)
        st.markdown("### " + labels[idx])
        st.image(Image.open(crops["img_path"] + imgs[idx]), width=150)

        df = pd.DataFrame({ 'labels': labels, 'data':result})
        df['data'] = df['data'].apply(lambda x : round(x*100,))
        df = df.sort_values(by=['data'], ascending=False)
        df = df.head(3)
        st.header("")

        st.write(descs[idx])

    
