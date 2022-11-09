import streamlit as st
import xgboost as xgb
import numpy as np
import pandas as pd
import altair as alt
import json
from PIL import Image

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

class_len = 22


loaded_model = xgb.Booster({'nthread': 4})
loaded_model.load_model('XB.model')


def analyze(input_data):
    label = np.random.randint(22, size=1)
    dtrain = xgb.DMatrix(np.array([input_data]), label=label)
    pred = loaded_model.predict(dtrain)
    return pred[0]

input_values = np.zeros(7)

st.title("Crop Recomendation Web App")
col1, col2 = st.columns(2)

with col1:
    input_values[0] = st.slider('Ratio of Nitrogen content in soil (%)', .0, 100.0, value=90.0)
    input_values[1] = st.slider('Ratio of Phosphorous content in soil (%)', .0, 100.0, value=42.5)
    input_values[2] = st.slider('Ratio of Potassium content in soil (%)', .0, 100.0, value=43.4)
    input_values[3] = st.number_input('Temperature (°C)', value=20.2)
    # input_values[4] = st.slider('Relative humidity (%)', .0, 100.0, value=82.1)
    input_values[4] = st.number_input('Relative humidity (%)', value=82.5)
    input_values[5] = st.number_input('pH value of the soil', value=6.5)
    input_values[6] = st.number_input('Rainfall intensity (mm)', value=200.9)

with col2:
    new_title = """
    <div style="border-style: solid;padding: 10px;border-radius: 10px;border-width: 1px;margin: 5px;">
        <h6> Costumize inputs to desired values! </h6>
        <p style="text-align: center; text-size: "> The output will be updated once the input changed </p>
    </div>
    """

    st.markdown(new_title, unsafe_allow_html=True)
    st.header("")
    st.header("")
    with st.spinner('Wait for it...'):
        result = analyze(input_values)
        idx = np.argmax(result)
        st.markdown("### " + labels[idx])
        st.image(Image.open(crops["img_path"] + imgs[idx]), width=150)

        df = pd.DataFrame({ 'labels': labels, 'data':result})
        df['data'] = df['data'].apply(lambda x : round(x*100,))
        df = df.sort_values(by=['data'], ascending=False)
        df = df.head(3)
        st.header("")
        st.header("")
        chart = (alt.Chart(df).mark_bar().encode(
                    x=alt.X("data", title="Probability"),
                    y=alt.Y("labels", title=" ", sort='-x')
                ))
        st.altair_chart(chart, use_container_width=True)

    
