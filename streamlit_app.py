import streamlit as st
import json
import requests
import pickle
import pandas as pd 
import numpy as np
import plotly.express as px


#----------------------------Import file---------------------------------#
df = pickle.load(open("dataset/df_for_deployment.pkl","rb"))
df = pd.DataFrame(df)
mapbox_access_token =  'pk.eyJ1Ijoiam9lbGpydCIsImEiOiJjbGJqaW12enYxM3M3M3hvZ2M1dzk3MThxIn0.xk3qkRogSnlc-wml2x63kQ'
px.set_mapbox_access_token(mapbox_access_token)


fig = px.scatter_mapbox(df, 
                        lat="latitude", 
                        lon="longitude",     
                        color="zone_code", 
                        size="count",
                        hover_name = "school",
                        color_continuous_scale=px.colors.cyclical.IceFire,
                        mapbox_style="dark",
                        size_max=10, 
                        zoom=9.2,
                       width=455, height=420)

#----------------------------Functions---------------------------------#
#def prayer_count(number,school):
    #original_count = df.loc[school,"count"]
    #original_count = original_count + number
    #df.loc[school.upper(),['count']] = original_count
    #st.session_state.df = df
    #return  

#----------------------------code---------------------------------#
st.title("Map Of Revival #H21:fire::fire::fire:")

plot_spot = st.empty()
school = st.selectbox('Select school being prayed for revival',(df["school"]), index = 0)
number = st.number_input(label = 'Number of people', step = 1, min_value = 1)

@st.cache
def update_revival_map(df, school, number):
    original_count = df.loc[school,"count"]
    original_count +=  number
    df.loc[school.upper(),['count']] = original_count

    fig = px.scatter_mapbox(df, 
                        lat="latitude", 
                        lon="longitude",     
                        color="zone_code", 
                        size="count",
                        hover_name = "school",
                        color_continuous_scale=px.colors.cyclical.IceFire,
                        mapbox_style="dark",
                        size_max=10, 
                        zoom=9.2,
                       width=455, height=420)

    return fig

if 'df' not in st.session_state:
    st.session_state.df = df

if st.button('Update revival map'):
    with plot_spot:
        fig = update_revival_map(st.session_state.df, school, number)
        st.plotly_chart(fig)


#fig.update_traces(cluster=dict(enabled=True))
with plot_spot:
    st.plotly_chart(fig)