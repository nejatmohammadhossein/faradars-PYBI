import streamlit as st
import pandas as pd
import datetime
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

#Read
df = pd.read_excel("Superstore.xlsx")

#Show output
image = Image.open("faradars.png")
col1, col2 = st.columns([0.1,0.9])
with col1:
    st.image(image,width=20)