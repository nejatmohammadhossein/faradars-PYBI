import streamlit as st
import pandas as pd
import datetime
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

#Read
df = pd.read_excel("Superstore.xlsx")
