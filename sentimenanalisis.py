import streamlit as st
import tensorflow as tf
import numpy as np

labels = ["apple","banana","blackgram","chickpea","coconut","coffee","cotton","grapes","jute","kidneybeans","lentil","maize","mango","mothbeans","mungbean","muskmelon","orange","papaya","pigeonpeas","pomegranate","rice","watermelon"]

class_len = 22

st.title("Sentiment Analysis Web App")

loaded_model = tf.keras.models.load_model("lstm.h5")

col1, col2 = st.columns(2)

tokenizer = None
model = None

def analyze(N, P, K, temp, humd, ph, rain):
    data = np.array([N, P, K, temp, humd, ph, rain])
    data = data.reshape(1, 7, 1)
    pred = loaded_model.predict(data)
    return pred

with col1:
    st.radio(
        "Select Sentiment Analysis Model: 👉",
        key="Model",
        options=labels,
    )

with col2:

    if st.button("Load Model"):
        with st.spinner('Wait for it...'):
            print("ok")
            # selected_idx = .index(st.session_state.Model)
            # # models[selected_idx].load()
            # idx = selected_idx
        st.success('Done!')

    txt = st.text_area('Text to analyze', 'selamat pagi')

    if st.button("ANALYZE"):
        result = analyze(90, 42 ,43 ,20.87,82.00,6.50,202.93)
        
        d = {l: i for l,i in zip(labels, result[0].tolist())}
        sortedD = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

        print(sortedD)

        st.write(np.argmax(result))


    
