import streamlit as st
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

st.title("Crop Recomendation Web App")
