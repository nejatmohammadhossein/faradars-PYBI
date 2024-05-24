import streamlit as st
import pandas as pd
import datetime
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

#Read
df = pd.read_excel("Superstore.xlsx")
st.set_page_config(layout="wide")
image = Image.open("faradars.png")
col1,col2 = st.columns([0.9,0.1])
with col2:
    st.image(image,width=100)

html_title="""
    <style>
    .title_test{
    font_weight:bold;
    padding:5px;
    border-radius:6px;
    font-family: 'B Titr'
    }
    </style>
    <center><h1 class="title_test">آموزش هوش تجاری داشبورد فروش</h1></center>"""
with col1:
    st.markdown(html_title,unsafe_allow_html=True)
