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
    border-radius:6px;
    font-family: 'B Titr'
    }
    </style>
    <center><h1 class="title_test">آموزش هوش تجاری داشبورد فروش</h1></center>"""
with col1:
    st.markdown(html_title,unsafe_allow_html=True)
st.divider()
col3, col4 = st.columns([0.45,0.45])
with col4:
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['year'] = df["Order Date"].dt.year
    years = sorted(df["year"].unique())
    years.insert(0,'همه سال ها')
    st.markdown('<p class="chart_title">فروش سالانه</p>',unsafe_allow_html=True)
    selected_year = st.selectbox('سال را انتخاب کنید',years)
    
    if selected_year != 'همه سال ها':
        filtered_df = df[df["year"] == selected_year]
    else:
        filtered_df = df

    fig = px.bar(filtered_df, x="Category",y="Sales", 
                 labels={"Sales":"فروش","Category":"گروه محصولات"},
                 #title='فروش سالانه',
                 hover_data=["Sales"],
                 height=500)
    fig.update_layout(
        #title='فروش سالانه',
        xaxis_title='گروه محصولات',
        yaxis_title='فروش',
        font=dict(family="tahoma"),
        yaxis=dict(title_standoff=50)
    )   
    st.markdown(
        """
        <style>
        body{
        direction:rtl !important;;
        font-family: 'B Titr';
        }
        .chart_title{
        font-weight:bold;
        font-family:'tahoma';
        text-align:center;
        }
        </style>
        """,unsafe_allow_html=True,
    )
    st.plotly_chart(fig, use_container_width=True)
key1 = 'selectbox1'
key2 = 'selectbox2'
key3 = 'selectbox3'
with col3:
    
    df['year'] = df["Order Date"].dt.year
    df['month'] = df["Order Date"].dt.month
    years = sorted(df["year"].unique())
    categories = sorted(df["Category"].unique())
    years.insert(0,'همه سال ها')
    categories.insert(0,'همه گروه های محصول')
    st.markdown('<p class="chart_title">فروش ماهانه</p>',unsafe_allow_html=True)
    col31,col32 = st.columns([0.5,0.5])
    with col31:
        selected_year = st.selectbox('سال را انتخاب کنید',years,key = key1)
    with col32:
        selected_category = st.selectbox('گروه محصول را انتخاب کنید',categories,key = key2)
    
    if selected_year != 'همه سال ها':
        filtered_df = df[df["year"] == selected_year]
    elif selected_category == 'همه گروه های محصول':
        filtered_df = df
    if selected_category != 'همه گروه های محصول':
        filtered_df = filtered_df[filtered_df["Category"] == selected_category]
    elif selected_year == 'همه سال ها':
        filtered_df = df
    result = filtered_df.groupby(by=filtered_df["month"])["Sales"].sum().reset_index()
    
    month_2 = ["ژانویه", "فوریه", "مارس", "آوریل", "مه", "ژوئن",
          "ژوییه", "اوت", "سپتامبر", "اکتبر", "نوامبر", "دسامبر"]
    result["month2"] = month_2
    print(result)
    fig = px.line(result, x="month2",y="Sales", 
                 #labels={"Sales":"فروش","Category":"گروه محصولات"},
                 #title='فروش سالانه',
                 hover_data=["Sales"],
                 height=500)
    fig.update_layout(
        #title='فروش سالانه',
        xaxis_title='ماه',
        yaxis_title='فروش',
        #font=dict(family="tahoma"),
        xaxis=dict(
            title=dict(
                font=dict(
                    family="tahoma",
                    color="blue"
                )
            ),
            tickfont=dict(
                family="tahoma",
                color="blue"
            )
        ),
        yaxis=dict(
            title_standoff=50,
            title=dict(
                font=dict(
                    family="tahoma",
                    color="blue"
                )
            ),
            tickfont=dict(
                family="tahoma",
                color="blue"
            )
        )
    )   
    
    st.plotly_chart(fig, use_container_width=True)

st.divider()

df['year'] = df["Order Date"].dt.year
years = sorted(df['year'].unique())
years.insert(0,"همه سال ها")
selected_years = st.multiselect("سالها را انتخاب کنید",
                                years, default ="همه سال ها",
                                key = key3)
if "همه سال ها" in selected_years:
    filtered_df =df
else:
    filtered_df = df[df["year"].isin(selected_years)]
result1 = filtered_df.groupby(by="State")[["Sales","Quantity"]].sum().reset_index()
#print(result1)
fig3 = go.Figure()
fig3.add_trace(go.Bar(x=result1["State"],
                      y=result1["Sales"],
                      name="فروش دلاری"))
fig3.add_trace(go.Scatter(x=result1["State"],y=result1["Quantity"],
                          mode="lines",yaxis="y2",
                          name="فروش مقداری"))
fig3.update_layout(
    xaxis_title='ایالت',
    yaxis_title=' فروش دلاری',
        #font=dict(family="tahoma"),
    xaxis=dict(
        title=dict(
            font=dict(
                family="tahoma",
                color="blue"
            )
        ),
        tickfont=dict(
            family="tahoma",
            color="blue"
        ), title_standoff=100
    ),
    yaxis=dict(
        title=dict(
            font=dict(
                family="tahoma",
                color="blue"
            )
        ),
        tickfont=dict(
            family="tahoma",
            color="blue"
        ), title_standoff=50
    ),
    yaxis2=dict(overlaying="y",side="right",
                title=dict(text="فروش مقداری",
                    font=dict(
                        family="tahoma",
                        color="blue"
                    )
                ),title_standoff=50),
    legend=dict(x=1,y=1.5),
    template="gridon"
)
_,col6 = st.columns([0.00001,1])
with col6:
    st.plotly_chart(fig3,use_container_width=True)

